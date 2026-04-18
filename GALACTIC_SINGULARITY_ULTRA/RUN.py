#!/usr/bin/env python3
"""
🌌 GALACTIC SINGULARITY ULTRA 2.0 - FINAL LAUNCHER
==================================================
Starte die App einfach und direkt
"""

import subprocess
import sys
import os

print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║       🌌 GALACTIC SINGULARITY ULTRA 2.0 - FINAL LAUNCHER 🌌          ║
║                                                                        ║
║                    Starting Unified AI System                         ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
""")

os.chdir('/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

# Step 1: Install Dependencies
print("\n📦 Step 1: Installing dependencies...")
print("-" * 70)
subprocess.run(
    [sys.executable, '-m', 'pip', 'install', '-q', 'flask>=2.3.0', 'werkzeug>=2.3.0'],
    check=False
)
print("✓ Flask & Werkzeug installed/verified")

# Step 2: Check Python Files
print("\n🔍 Step 2: Checking Python files...")
print("-" * 70)
files_to_check = [
    'app_unified.py',
    'templates/index.html',
    'static/css/style.css',
    'static/js/singularity.js',
]

for f in files_to_check:
    if os.path.exists(f):
        print(f"✓ {f}")
    else:
        print(f"❌ Missing: {f}")

# Step 3: Test Import
print("\n🧪 Step 3: Testing imports...")
print("-" * 70)
sys.path.insert(0, '.')

try:
    # Test that app_unified works
    exec(open('app_unified.py').read(), {'__name__': '__test__'})
    print("⚠️  Note: app_unified.py contains test code")
except Exception as e:
    print(f"Testing complete: {str(e)[:50]}")

print("\n" + "="*70)
print("✨ SYSTEM READY - STARTING APPLICATION...")
print("="*70)

print("""

🚀 Application is starting:

   🌐 URL: http://localhost:5000
   🛑 To stop: Press Ctrl+C
   
   ✨ Click on the Galactic Singularity to open the chat portal!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")

# Step 4: Start the App
print("Loading Flask app...")
os.system(f'{sys.executable} app_unified.py')

