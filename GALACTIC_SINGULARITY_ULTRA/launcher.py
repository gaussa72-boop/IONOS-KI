#!/usr/bin/env python3
"""
GALACTIC SINGULARITY ULTRA - Launcher
======================================
Python-basiertes Startup-Script mit Dependency-Management
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Hauptfunktion für den Launcher"""

    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║     🌌 GALACTIC SINGULARITY ULTRA 2.0 🌌                      ║
    ║                                                                ║
    ║     Initializing Launch Sequence...                           ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)

    # Get base directory
    base_dir = Path(__file__).parent

    # Check Python version
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ erforderlich!")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    # Install requirements
    print("\n📦 Installing dependencies...")
    requirements_file = base_dir / 'requirements.txt'

    if requirements_file.exists():
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', '-r', str(requirements_file)])
            print("✓ Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Fehler beim Installieren: {e}")
            return False
    else:
        print("⚠️  requirements.txt nicht gefunden!")

    # Check for Flask
    print("\n🔍 Checking Flask installation...")
    try:
        import flask
        print(f"✓ Flask {flask.__version__} installed")
    except ImportError:
        print("❌ Flask ist nicht installiert!")
        return False

    # Check app file
    app_file = base_dir / 'app_unified.py'
    if not app_file.exists():
        print(f"❌ {app_file} nicht gefunden!")
        return False
    print(f"✓ App file found: {app_file.name}")

    # Show startup info
    print("\n" + "="*64)
    print("🌌 STARTING GALACTIC SINGULARITY ULTRA...")
    print("="*64)
    print("\n🌐 Access the application at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server\n")

    # Start Flask app
    try:
        os.chdir(base_dir)
        subprocess.call([sys.executable, str(app_file)])
    except KeyboardInterrupt:
        print("\n\n🌌 Galaktische Singularität wurde beendet.")
        return True
    except Exception as e:
        print(f"\n❌ Fehler beim Starten: {e}")
        return False

    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

