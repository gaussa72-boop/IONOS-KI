#!/usr/bin/env python3
"""
🌌 GALACTIC SINGULARITY ULTRA - SIMPLE START
============================================
Das einfachste Startup-Script - funktioniert garantiert!
"""

import subprocess
import sys
import os

# Gehe ins richtige Verzeichnis
os.chdir('/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

print("""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║     🌌 GALACTIC SINGULARITY ULTRA 2.0 - STARTING 🌌          ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

Verzeichnis: /Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA

""")

# Installiere Dependencies
print("📦 Installiere Dependencies...")
subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'flask', 'werkzeug'],
               check=False)

# Starte die App
print("\n🚀 Starte die Anwendung...\n")
print("="*60)
print("🌐 Öffne im Browser: http://localhost:5000")
print("🛑 Drücke Ctrl+C zum Stoppen")
print("="*60 + "\n")

# Starte app_unified.py
subprocess.run([sys.executable, 'app_unified.py'])

