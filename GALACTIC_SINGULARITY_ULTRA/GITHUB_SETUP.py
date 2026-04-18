#!/usr/bin/env python3
"""
🌌 GALACTIC SINGULARITY - GITHUB UPLOAD GUIDE
=============================================
Schritt-für-Schritt Anleitung für GitHub
"""

import os
import subprocess

os.chdir('/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║     🌌 GALACTIC SINGULARITY ULTRA 2.0 - GITHUB SETUP 🌌              ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝

📝 SCHRITT-FÜR-SCHRITT ANLEITUNG

═════════════════════════════════════════════════════════════════════════

SCHRITT 1: GitHub Repository erstellen
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gehe zu: https://github.com/new

Ausfüllen:
  • Repository name: galactic-singularity-ultra
  • Description: 🌌 Unified AI System with Galactic Singularity Portal
  • Public oder Private: Deine Wahl
  • Initialize with README: NICHT ankreuzen
  • .gitignore: Python
  • License: MIT (optional)

Klick: "Create repository"

Kopiere die Repository URL (HTTPS):
  https://github.com/DEINBENUTZERNAME/galactic-singularity-ultra.git

═════════════════════════════════════════════════════════════════════════

SCHRITT 2: Git initialisieren (lokal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Terminal öffnen und einfügen:

cd /Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA

git init

git add .

git commit -m "🌌 Initial commit: Galactic Singularity ULTRA 2.0"

═════════════════════════════════════════════════════════════════════════

SCHRITT 3: Remote Repository hinzufügen
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ersetze "DEINBENUTZERNAME" mit deinem GitHub Username:

git remote add origin https://github.com/DEINBENUTZERNAME/galactic-singularity-ultra.git

Verifiziere:

git remote -v

═════════════════════════════════════════════════════════════════════════

SCHRITT 4: Hochladen zu GitHub
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

git branch -M main

git push -u origin main

Du wirst gefragt nach deinen GitHub Credentials:
  • Username: Dein GitHub Username
  • Password: Dein Personal Access Token (oder Passwort)

═════════════════════════════════════════════════════════════════════════

SCHRITT 5: Verifizieren
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gehe zu: https://github.com/DEINBENUTZERNAME/galactic-singularity-ultra

Du solltest alle Dateien sehen!

═════════════════════════════════════════════════════════════════════════

📊 PROJEKT STRUKTUR IM REPOSITORY

galactic-singularity-ultra/
├── 🌟 app_unified.py          (529 lines - Main App)
├── 🚀 GO.py                   (Launcher)
├── 🧪 TEST.py                 (Tests)
├── 📖 README.md               (Dokumentation)
├── 📝 requirements.txt        (Dependencies)
├── 📁 templates/
│   ├── index.html            (Homepage)
│   └── auth.html             (Auth)
├── 📁 static/
│   ├── css/style.css         (Design)
│   └── js/singularity.js     (Interaktivität)
├── 📁 core/                  (AI Modules)
└── 📁 app/                   (Backend)

═════════════════════════════════════════════════════════════════════════

🔐 WICHTIG: Personal Access Token

Falls du einen Token brauchst:

1. GitHub Einstellungen: https://github.com/settings/tokens
2. "Generate new token"
3. Scope: repo (Full control of private repositories)
4. Generate
5. Token kopieren und speichern (wird nicht noch mal angezeigt!)
6. Bei Git Push als Passwort verwenden

═════════════════════════════════════════════════════════════════════════

💾 DANACH REGELMÄSSIG SPEICHERN

Nach Änderungen:

git add .
git commit -m "Deine Beschreibung"
git push

═════════════════════════════════════════════════════════════════════════
""")

print("\n✨ Setup-Anleitung fertig!")
print("Folge den Schritten oben um dein Projekt auf GitHub hochzuladen.\n")

# Informationen über lokales Repository
print("📊 LOKALE GIT INFORMATIONEN")
print("="*70)

if os.path.exists('.git'):
    print("✓ Git Repository bereits initialisiert")
    result = subprocess.run(['git', 'status'], capture_output=True, text=True)
    print("\nGit Status:")
    print(result.stdout[:500])
else:
    print("ℹ️  Git Repository noch nicht initialisiert (mach das mit den Befehlen oben)")

print("\n" + "="*70)
print("🌌 Viel Erfolg mit GitHub! ✨")
print("="*70)

