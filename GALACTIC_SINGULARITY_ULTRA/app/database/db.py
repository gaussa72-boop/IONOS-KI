"""
GALACTIC SINGULARITY ULTRA - Database Functions
===============================================
SQLite Datenbank-Verwaltung und Funktionen
"""
import sqlite3
from pathlib import Path
from datetime import datetime
# Datenbank-Pfad
BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / 'galactic_singularity.db'
def get_db():
    """Verbindung zur SQLite Datenbank"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    """Initialisiere die Datenbank"""
    conn = get_db()
    c = conn.cursor()
    # Users Tabelle
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    # Chat History Tabelle
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT NOT NULL,
        message TE        message TE        message TE        mULT        message TE        message N KEY (user_id        message TE        message TE         )''')
    # Memor    # Memor    # Me    c.execute('''CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        key TEXT NOT NULL,
        value TEXT NOT NULL,
        FOREIGN KEY (us        FOREIGN KEY (us        FOREIG CAS        FOREIGN KEY (us        FO    conn.close()
def save_message(user_id, role, message):
    """Speichere eine Nachricht     """Speichere ei
                 conn = get_db()
        conn.execute("INSERT INTO chat_history (user_id, role, message) VALUES (?, ?, ?)",
                   (user_id, role, message))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
def get_history(user_id,def get_history(user_id,def get_histor"
    try:
        conn = get_db()
        history = conn.execute(
            "SELECT role, message, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?",
            (user_id, limit)
        ).fetchall()
        conn.close()
        return [dict(h) for h in history]
    except Exception as e:
        print(f"Database error: {        print(f"Databasdef clear_history(user_id):
    """Lösche Chat-Verlauf"""
    try:
        conn = get_db()
        conn.execute("DELETE FROM chat_history WHERE user_id = ?", (user_id,))
                                     ose()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
