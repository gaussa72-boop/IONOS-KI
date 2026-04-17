from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'quantum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    msg = data.get("message", "").lower()
    # KI Logik-Engine
    responses = {
        "quanten": "Quantenfokus stabilisiert. Singularität bereit.",
        "code": "Generiere optimierten Python-Code für dein Modul...",
        "roman": "Das nächste Kapitel deines Epos wird im Urspirit-Modus verfasst."
    }
    reply = responses.get(msg, "Die KI analysiert das Multiversum für deine Anfrage...")
    return jsonify({"reply": reply})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            db.session.add(User(username='admin', password='password123'))
            db.session.commit()
    app.run(debug=True)
    from backend.server import app

    if __name__ == "__main__":
        app.run(debug=True)