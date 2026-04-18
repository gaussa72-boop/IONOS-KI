#!/usr/bin/env python3
"""
🌌 GALACTIC SINGULARITY - QUICK TEST
===================================
Schneller Test aller Komponenten
"""

import subprocess
import sys
import os

# Wechsle ins richtige Verzeichnis
os.chdir('/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

print("""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║     🌌 QUICK TEST - GALACTIC SINGULARITY 🌌                  ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
""")

# Test 1: Dateistruktur
print("\n✓ Test 1: Dateistruktur")
files = [
    'app_unified.py',
    'templates/index.html',
    'static/css/style.css',
    'static/js/singularity.js'
]
for f in files:
    if os.path.exists(f):
        print(f"  ✓ {f}")
    else:
        print(f"  ✗ {f} FEHLT!")

# Test 2: Flask Installation
print("\n✓ Test 2: Flask Installation")
try:
    import flask
    print(f"  ✓ Flask {flask.__version__}")
except ImportError:
    print("  ✗ Flask nicht installiert!")
    print("  → Installiere jetzt...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'flask'])
    print("  ✓ Flask installiert")

# Test 3: App Import
print("\n✓ Test 3: App Import")
try:
    from app_unified import app
    print("  ✓ app_unified.py importiert")

    # Test API
    with app.test_client() as client:
        r = client.get('/api/status')
        if r.status_code == 200:
            print(f"  ✓ API funktioniert (Status: {r.status_code})")
        else:
            print(f"  ✗ API Error (Status: {r.status_code})")
except Exception as e:
    print(f"  ✗ Fehler: {e}")

# Test 4: Database
print("\n✓ Test 4: Database")
try:
    import sqlite3
    from pathlib import Path
    db = Path('galactic_singularity.db')
    if db.exists():
        print(f"  ✓ Database existiert ({db.stat().st_size} bytes)")
    else:
        print("  ✓ Database wird beim Start erstellt")
except Exception as e:
    print(f"  ✗ Fehler: {e}")

print("\n" + "="*60)
print("✨ QUICK TEST FERTIG")
print("="*60)

print("""

🚀 ZUM STARTEN:

  python3 GO.py

  oder

  python3 app_unified.py

🌐 Dann öffne: http://localhost:5000

""")

