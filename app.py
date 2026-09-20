import os
import time
import urllib.request
import urllib.error
import json
from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-change-me")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///users.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.get("/health")
def health():
    return jsonify({"status":"ok","project":"IONOS-KI","version":"IONOS 7","model":os.getenv("OPENAI_MODEL","gpt-6-astra"),"game_engine":"active","time":int(time.time())})

@app.get("/engine")
def engine():
    return send_from_directory(".", "game_engine.html")

@app.get("/game_engine.js")
def engine_js():
    return send_from_directory(".", "game_engine.js")

@app.get("/")
def index():
    return render_template("index.html", user=(current_user.username if current_user.is_authenticated else "Adriano Gauß"))

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=(request.form.get("username") or "").strip()
        password=request.form.get("password") or ""
        if not username or not password: return "Benutzername und Passwort erforderlich.",400
        if User.query.filter_by(username=username).first(): return "Benutzername existiert bereits.",409
        db.session.add(User(username=username,password=generate_password_hash(password)))
        db.session.commit()
        return '<script>location.href="/login"</script>'
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=(request.form.get("username") or "").strip()
        password=request.form.get("password") or ""
        user=User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            return '<script>location.href="/"</script>'
        return "Ungültige Anmeldedaten.",401
    return render_template("login.html")

@app.get("/logout")
def logout():
    logout_user()
    return '<script>location.href="/"</script>'

def _local_reply(message):
    m=message.lower()
    if any(k in m for k in ("code","python","javascript","html","css","github","render")):
        return "Ich habe den technischen Kontext erkannt. Ich kann Architektur, Code, Tests und Deployment-Schritte strukturieren und die Antwort in konkrete nächste Aktionen zerlegen."
    if any(k in m for k in ("idee","projekt","bauen","app","webseite","notiz")):
        return "Idee erkannt. Ich zerlege sie in Ziel, Anforderungen, Architektur, Umsetzung, Tests und nächste Schritte."
    if any(k in m for k in ("bild","design","logo","ui")):
        return "Design-Modus aktiv. Ich kann Layout, Komponenten, Typografie, Abstände und responsive Verhalten als umsetzbare Spezifikation ausarbeiten."
    if any(k in m for k in ("lernen","erkläre","warum","wie")):
        return "Erklärmodus aktiv. Ich strukturiere das Thema verständlich, nenne Annahmen und trenne Fakten, Beispiele und offene Punkte."
    return "IONOS-KI hat deine Anfrage analysiert. Ich kann Wissen strukturieren, Ideen in Projekte übersetzen, Code erzeugen und komplexe Aufgaben in überprüfbare Schritte zerlegen."

def _openai_reply(message, history):
    api_key=os.getenv("OPENAI_API_KEY")
    if not api_key: return None
    model=os.getenv("OPENAI_MODEL","gpt-5.6")
    payload={"model":model,"messages":[
        {"role":"system","content":"Du bist IONOS-KI V2, ein vielseitiger KI-Assistent. Arbeite präzise, strukturiert und ehrlich. Behaupte keine nicht ausgeführten Aktionen. Bei Code liefere robuste, wartbare Lösungen und weise auf fehlende Secrets oder Tests hin."},
        *history[-10:],{"role":"user","content":message}
    ],"temperature":0.4}
    req=urllib.request.Request("https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization":f"Bearer {api_key}","Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=45) as resp:
            data=json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"].strip()
    except (urllib.error.URLError,KeyError,IndexError,json.JSONDecodeError):
        return None

@app.post("/api/chat")
def chat():
    data=request.get_json(silent=True) or {}
    message=(data.get("message") or "").strip()
    if not message: return jsonify({"error":"message is required"}),400
    history=session.get("chat_history",[])
    reply=_openai_reply(message,history) or _local_reply(message)
    history.extend([{"role":"user","content":message},{"role":"assistant","content":reply}])
    session["chat_history"]=history[-12:]
    return jsonify({"reply":reply,"mode":"openai" if os.getenv("OPENAI_API_KEY") else "local"})

@app.post("/api/reset")
def reset_chat():
    session.pop("chat_history",None)
    return jsonify({"ok":True})

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.getenv("PORT","10000")),debug=False)
