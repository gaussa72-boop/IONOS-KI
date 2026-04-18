#!/bin/bash
# 🌌 GALACTIC SINGULARITY ULTRA - FINAL START SCRIPT

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║     🌌 GALACTIC SINGULARITY ULTRA 2.0 🌌                      ║"
echo "║                                                                ║"
echo "║              STARTING PRODUCTION APPLICATION                  ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

echo "📦 Step 1: Checking Python..."
python3 --version

echo ""
echo "📦 Step 2: Installing dependencies..."
python3 -m pip install -q flask werkzeug 2>/dev/null || true

echo "✓ Dependencies ready"

echo ""
echo "🧪 Step 3: Verifying application..."
if [ -f "app_unified.py" ]; then
    echo "✓ app_unified.py found"
else
    echo "❌ app_unified.py not found!"
    exit 1
fi

if [ -f "templates/index.html" ]; then
    echo "✓ templates/index.html found"
else
    echo "❌ templates not found!"
    exit 1
fi

if [ -f "static/css/style.css" ]; then
    echo "✓ static files found"
else
    echo "❌ static files not found!"
    exit 1
fi

echo ""
echo "═════════════════════════════════════════════════════════════════"
echo "✨ SYSTEM READY - LAUNCHING APPLICATION"
echo "═════════════════════════════════════════════════════════════════"
echo ""
echo "🌐 Server URL: http://localhost:5000"
echo "🛑 To stop: Press Ctrl+C"
echo "🎯 Click on the Galactic Singularity to open the chat portal!"
echo ""

python3 app_unified.py

