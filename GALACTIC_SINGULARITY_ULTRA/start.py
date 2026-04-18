#!/usr/bin/env python3
"""
Quick Start - Galactic Singularity
"""
import subprocess
import sys
import os

os.chdir('/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

# Install Flask wenn nötig
print("📦 Installiere Flask...")
subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'flask', 'werkzeug'], check=False)

# Starte die App
print("🚀 Starte Galactic Singularity ULTRA...")
print("🌐 Öffne: http://localhost:5000\n")

subprocess.run([sys.executable, 'main.py'])

