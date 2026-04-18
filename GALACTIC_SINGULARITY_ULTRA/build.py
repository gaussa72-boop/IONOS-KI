#!/usr/bin/env python3
"""
GALACTIC SINGULARITY ULTRA - Build & Setup Script
==================================================
Vorbereitung und Start der Anwendung
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header(text):
    """Drucke einen schönen Header"""
    print("\n" + "="*70)
    print(text)
    print("="*70)

def main():
    """Hauptfunktion"""

    print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║      🌌 GALACTIC SINGULARITY ULTRA 2.0 - BUILD & SETUP 🌌            ║
║                                                                        ║
║              Vorbereitung der Anwendung für den Start                 ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
    """)

    # Get base directory
    base_dir = Path(__file__).parent
    os.chdir(base_dir)

    # STEP 1: Python Version Check
    print_header("SCHRITT 1: Python Version Check")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ erforderlich!")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    # STEP 2: Dependencies
    print_header("SCHRITT 2: Dependencies Installation")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'flask', 'werkzeug'])
        print("✓ Flask installiert")
        print("✓ Werkzeug installiert")
    except Exception as e:
        print(f"⚠️  Fehler: {e}")

    # STEP 3: Check Structure
    print_header("SCHRITT 3: Projektstruktur Check")
    required_files = [
        'core/__init__.py',
        'core/brain.py',
        'core/ai_modules.py',
        'core/agents.py',
        'app/__init__.py',
        'app/database/__init__.py',
        'app/database/db.py',
        'main.py',
        'templates/index.html',
        'static/css/style.css',
        'static/js/singularity.js',
    ]

    all_found = True
    for file_path in required_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"❌ FEHLT: {file_path}")
            all_found = False

    if not all_found:
        print("\n⚠️  Einige Dateien fehlen!")
        return False

    # STEP 4: Import Check
    print_header("SCHRITT 4: Import Check")
    sys.path.insert(0, str(base_dir))

    try:
        print("  Importing core.GalacticBrain...", end=" ")
        from core import GalacticBrain
        print("✓")

        print("  Importing core modules...", end=" ")
        from core.ai_modules import QuantumAI, LebensblumeAI, UrspiritAI
        from core.agents import SocialAgent, FinanceAgent, CreatorAgent
        print("✓")

        print("  Importing database...", end=" ")
        from app.database.db import init_db, get_db
        print("✓")

        print("  Importing Flask app...", end=" ")
        from main import app
        print("✓")

    except Exception as e:
        print(f"\n❌ Import Error: {e}")
        import traceback
        traceback.print_exc()
        return False

    # STEP 5: Database Setup
    print_header("SCHRITT 5: Datenbank Setup")
    try:
        init_db()
        print("✓ Datenbank initialisiert")
        conn = get_db()
        conn.close()
        print("✓ Datenbankverbindung getestet")
    except Exception as e:
        print(f"❌ Database Error: {e}")
        return False

    # STEP 6: Quick Test
    print_header("SCHRITT 6: Quick Functionality Test")
    try:
        brain = GalacticBrain()
        responses = brain.process("test")
        if responses and len(responses[0]) > 0:
            print(f"✓ Brain Processing: {responses[0][:40]}...")
        else:
            print("❌ Brain Processing failed")
            return False
    except Exception as e:
        print(f"❌ Brain Test Error: {e}")
        return False

    try:
        with app.test_client() as client:
            response = client.get('/api/status')
            if response.status_code == 200:
                print(f"✓ API Status: {response.status_code}")
            else:
                print(f"❌ API Status: {response.status_code}")
                return False
    except Exception as e:
        print(f"❌ API Test Error: {e}")
        return False

    # STEP 7: Ready to Launch
    print_header("✨ SYSTEM READY - ALLE CHECKS BESTANDEN! ✨")
    print("""
    
Die Anwendung ist bereit zum Start!

🚀 ZUM STARTEN:

    python3 main.py
    
🌐 DANN ÖFFNEN:

    http://localhost:5000
    
    Klick auf die 🌌 Galaktische Singularität!

═════════════════════════════════════════════════════════════════════════════

✓ Python 3.8+
✓ Dependencies installiert
✓ Projektstruktur vollständig
✓ Alle Imports funktionieren
✓ Datenbank initialisiert
✓ Brain funktioniert
✓ API funktioniert

🌌 Viel Spaß mit der Galaktischen Singularität! ✨

═════════════════════════════════════════════════════════════════════════════
    """)

    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

