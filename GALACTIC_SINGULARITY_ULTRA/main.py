#!/usr/bin/env python3
"""
GALACTIC SINGULARITY ULTRA 2.0 - Main Application
==================================================
Unified AI System mit galaktischer Singularität
"""

import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3

# Import Core Modules
from core import GalacticBrain
from app.database.db import init_db, save_message, get_history, clear_history, get_db

# =====================================================
# FLASK APP CONFIGURATION
# =====================================================

app = Flask(__name__,
    template_folder='templates',
    static_folder='static'
)
app.secret_key = os.environ.get("SECRET_KEY", "galactic_singularity_secret_2024")

# Initialize Database
init_db()

# Create Global Brain Instance
galactic_brain = GalacticBrain()

# =====================================================
# AUTHENTICATION ROUTES
# =====================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Benutzerregistrierung"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            return render_template('auth.html', mode='register', error='Alle Felder ausfüllen!')

        if len(username) < 3:
            return render_template('auth.html', mode='register', error='Username mind. 3 Zeichen!')

        if len(password) < 6:
            return render_template('auth.html', mode='register', error='Passwort mind. 6 Zeichen!')

        try:
            conn = get_db()
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, generate_password_hash(password)))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return render_template('auth.html', mode='register', error='Benutzername bereits vergeben!')
        except Exception as e:
            return render_template('auth.html', mode='register', error=f'Fehler: {str(e)}')

    return render_template('auth.html', mode='register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Benutzer-Login"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        try:
            conn = get_db()
            user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            conn.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('index'))

            return render_template('auth.html', mode='login', error='Ungültige Anmeldedaten!')
        except Exception as e:
            return render_template('auth.html', mode='login', error=f'Fehler: {str(e)}')

    return render_template('auth.html', mode='login')


@app.route('/logout')
def logout():
    """Benutzer ausloggen"""
    session.clear()
    return redirect(url_for('index'))

# =====================================================
# MAIN ROUTES
# =====================================================

@app.route('/')
def index():
    """Hauptseite mit der galaktischen Singularität"""
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """Chat-Endpoint für die KI-Kommunikation"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Keine Nachricht empfangen'}), 400

        # Limit Nachrichtenlänge
        user_message = user_message[:1000]

        # Verarbeite die Nachricht durch das galaktische Gehirn
        responses = galactic_brain.process(user_message)

        # Kombiniere alle Antworten
        full_response = "\n\n".join(responses)

        # Speichere in der Datenbank wenn eingeloggt
        user_id = session.get('user_id')
        if user_id:
            save_message(user_id, 'user', user_message)
            save_message(user_id, 'assistant', full_response)

        return jsonify({
            'response': full_response,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'error': f'Fehler: {str(e)}'}), 500


@app.route('/history')
def history():
    """Chat-Verlauf abrufen"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Nicht eingeloggt'}), 401

    try:
        history_data = get_history(user_id, limit=50)
        return jsonify(history_data)
    except Exception as e:
        return jsonify({'error': f'Fehler: {str(e)}'}), 500


@app.route('/api/status')
def api_status():
    """API Status Check"""
    return jsonify({
        'status': 'online',
        'name': 'GALACTIC SINGULARITY ULTRA',
        'version': '2.0.0',
        'modules': [
            'QuantumAI',
            'LebensblumeAI',
            'UrspiritAI',
            'SocialAgent',
            'FinanceAgent',
            'CreatorAgent'
        ],
        'openai_available': galactic_brain.openai_client is not None,
        'database': 'sqlite3',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/clear-history', methods=['POST'])
def api_clear_history():
    """Lösche Chat-Verlauf"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Nicht eingeloggt'}), 401

    try:
        if clear_history(user_id):
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Fehler beim Löschen'}), 500
    except Exception as e:
        return jsonify({'error': f'Fehler: {str(e)}'}), 500

# =====================================================
# ERROR HANDLERS
# =====================================================

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Nicht gefunden'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server-Fehler'}), 500

# =====================================================
# MAIN
# =====================================================

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║     🌌 GALACTIC SINGULARITY ULTRA 2.0 🌌                      ║
    ║                                                                ║
    ║     Unified AI System - Alle Module integriert                ║
    ║     Modularisierte Architektur mit sauberer Struktur          ║
    ║                                                                ║
    ║     Features:                                                 ║
    ║     ⚛️  Quantum AI - Raumzeit-Manipulation                    ║
    ║     🌸 Lebensblume AI - Heilige Geometrie                    ║
    ║     🕉️  Urspirit AI - Bewusstseinsfeld                       ║
    ║     💰 Finance Agent - Wohlstands-Energie                    ║
    ║     🎨 Creator Agent - Kreative Kraft                        ║
    ║     📢 Social Agent - Gemeinschafts-Energie                  ║
    ║     🔗 OpenAI Integration (optional)                         ║
    ║     🔐 Benutzer-Authentifizierung & Chat-Verlauf            ║
    ║                                                                ║
    ║     Klicke auf die Singularität um das Portal zu öffnen      ║
    ║     Server: http://localhost:5000                            ║
    ║     Press Ctrl+C zum Stoppen                                 ║
    ║                                                                ║
    ║     Projektstruktur:                                          ║
    ║     📁 core/ - AI Module und Brain                            ║
    ║     📁 app/ - Flask Anwendung und Routes                      ║
    ║     📁 templates/ - HTML Templates                           ║
    ║     📁 static/ - CSS und JavaScript                          ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)

    app.run(host='0.0.0.0', port=5000, debug=True)

