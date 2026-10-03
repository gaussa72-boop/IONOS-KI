import os
import time
import urllib.request
import urllib.error
import json
from flask import Flask, jsonify, render_template, request, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)

# SECURITY HARDENING
from collections import defaultdict, deque
from time import monotonic
_SEC_RATE=defaultdict(deque)
@app.before_request
def _sec_before():
    if request.content_length and request.content_length > 1048576: return jsonify(error="Request too large."),413
    if request.path in {"/.env","/.git/config","/server.py","/app.py","/main.py","/package.json","/requirements.txt","/render.yaml","/Procfile"} or request.path.startswith("/.git/") or request.path.startswith("/.env"): return jsonify(error="Not Found."),404
    q=_SEC_RATE[request.remote_addr or "unknown"]; now=monotonic()
    while q and now-q[0]>60:q.popleft()
    if len(q)>=(30 if request.method in {"POST","PUT","PATCH","DELETE"} else 120): return jsonify(error="Too many requests. Please try again later."),429
    q.append(now)
@app.after_request
def _sec_headers(response):
    response.headers.setdefault("X-Content-Type-Options","nosniff")
    response.headers.setdefault("X-Frame-Options","DENY")
    response.headers.setdefault("Referrer-Policy","strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy","camera=(), microphone=(), geolocation=()")
    response.headers.setdefault("Cross-Origin-Opener-Policy","same-origin")
    response.headers.setdefault("Strict-Transport-Security","max-age=31536000; includeSubDomains")
    if request.path.startswith("/api/"): response.headers["Cache-Control"]="no-store"
    response.headers.pop("Server",None)
    return response


# --- Security hardening ---
from collections import defaultdict, deque
from time import monotonic
from html import escape as html_escape

_SECURITY_RATE = defaultdict(deque)
_SECURITY_WINDOW = 60
_SECURITY_MAX = 120
_SECURITY_POST_MAX = 30
_SECURITY_MAX_BODY = 1024 * 1024

@app.before_request
def _security_before_request():
    if request.content_length and request.content_length > _SECURITY_MAX_BODY:
        return jsonify(error="Request too large."), 413
    path = request.path or "/"
    blocked = {"/.env","/.git/config","/server.py","/app.py","/main.py","/package.json","/requirements.txt","/render.yaml","/Procfile"}
    if path in blocked or path.startswith("/.git/") or path.startswith("/.env"):
        return jsonify(error="Not Found."), 404
    ip = request.remote_addr or "unknown"
    now = monotonic()
    q = _SECURITY_RATE[ip]
    while q and now - q[0] > _SECURITY_WINDOW:
        q.popleft()
    limit = _SECURITY_POST_MAX if request.method in {"POST","PUT","PATCH","DELETE"} else _SECURITY_MAX
    if len(q) >= limit:
        return jsonify(error="Too many requests. Please try again later."), 429
    q.append(now)

@app.after_request
def _security_headers(response):
    response.headers.setdefault("X-Content-Type-Options","nosniff")
    response.headers.setdefault("X-Frame-Options","DENY")
    response.headers.setdefault("Referrer-Policy","strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy","camera=(), microphone=(), geolocation=()")
    response.headers.setdefault("Cross-Origin-Opener-Policy","same-origin")
    response.headers.setdefault("Strict-Transport-Security","max-age=31536000; includeSubDomains")
    response.headers.setdefault("Cache-Control","no-store" if request.path.startswith("/api/") else "public, max-age=300")
    response.headers.pop("Server", None)
    return response
# --- End security hardening ---
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or (_ for _ in ()).throw(RuntimeError("SECRET_KEY must be configured"))
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///users.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
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
    return jsonify({"status":"ok","project":"IONOS-KI","version":"IONOS 7","model":os.getenv("OPENAI_MODEL","gpt-5.6"),"game_engine":"active","time":int(time.time())})

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

def _openai_reply(message, history, model=None):
    api_key=os.getenv("OPENAI_API_KEY")
    openrouter_key=os.getenv("OPENROUTER_API_KEY")
    selected=(model or os.getenv("OPENAI_MODEL","gpt-5.6")).strip()
    try:
        from openai import OpenAI
        if selected.startswith(("openai/","anthropic/","google/","x-ai/","deepseek/","mistralai/","z-ai/","qwen/")) and openrouter_key:
            client=OpenAI(api_key=openrouter_key, base_url="https://openrouter.ai/api/v1")
            actual=selected
        elif api_key:
            client=OpenAI(api_key=api_key)
            actual=selected.split("/",1)[-1] if selected.startswith("openai/") else os.getenv("OPENAI_MODEL","gpt-5.6")
        else:
            return None
        tools=[{"type":"web_search","search_context_size":"medium"}] if os.getenv("ENABLE_WEB_SEARCH","true").lower()=="true" else []
        response=client.responses.create(
            model=actual,
            reasoning={"effort":"high"},
            tools=tools,
            tool_choice="auto",
            store=False,
            input=[
                {"role":"system","content":"Du bist IONOS-KI V2. Arbeite präzise, strukturiert, kontextbewusst und ehrlich. Prüfe Annahmen, nutze Websuche für aktuelle Fakten und behaupte keine nicht ausgeführten Aktionen."},
                *history[-12:],
                {"role":"user","content":message}
            ]
        )
        return response.output_text.strip() if response.output_text else None
    except Exception:
        app.logger.exception("AI model request failed")
        return None

@app.get("/api/models")
def models():
    return jsonify({
        "default":"openai/gpt-5.6",
        "openrouter_configured":bool(os.getenv("OPENROUTER_API_KEY")),
        "models":[
            {"id":"openai/gpt-5.6","provider":"OpenAI","name":"GPT-5.6"},
            {"id":"anthropic/claude-sonnet-5.5","provider":"Anthropic","name":"Claude Sonnet 5.5"},
            {"id":"anthropic/claude-opus-5.5","provider":"Anthropic","name":"Claude Opus 5.5"},
            {"id":"google/gemini-3.8-flash","provider":"Google","name":"Gemini 3.8 Flash"},
            {"id":"google/gemini-3.1-pro-preview","provider":"Google","name":"Gemini 3.1 Pro"},
            {"id":"x-ai/grok-4.7","provider":"xAI","name":"Grok 4.7"},
            {"id":"deepseek/deepseek-v4-pro","provider":"DeepSeek","name":"V4 Pro"},
            {"id":"deepseek/deepseek-v4.1-flash","provider":"DeepSeek","name":"V4.1 Flash"},
            {"id":"mistralai/mistral-small-2603","provider":"Mistral","name":"Small 4"},
            {"id":"mistralai/mistral-medium-3.5","provider":"Mistral","name":"Medium 3.5"},
            {"id":"z-ai/glm-5.3","provider":"Z.ai","name":"GLM 5.3"},
            {"id":"qwen/qwen3-max","provider":"Qwen","name":"Qwen3 Max"}
        ]
    })

