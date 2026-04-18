#!/bin/bash
# GALACTIC SINGULARITY ULTRA - Startup Script
# =============================================

echo "🌌 Starten der Galaktischen Singularität..."
echo ""

# Prüfe ob Python installiert ist
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 ist nicht installiert!"
    exit 1
fi

echo "✓ Python 3 gefunden"

# Installiere Dependencies
echo ""
echo "📦 Installiere Dependencies..."
pip3 install -r requirements.txt

# Prüfe auf errors
if [ $? -ne 0 ]; then
    echo "❌ Fehler beim Installieren der Dependencies!"
    exit 1
fi

echo ""
echo "✓ Dependencies installiert"

# Starte das Programm
echo ""
echo "🚀 Starte GALACTIC SINGULARITY ULTRA..."
echo ""
python3 app_unified.py

# Wenn das Skript hier endet, zeige eine Abschlussmeldung
echo ""
echo "🌌 Galaktische Singularität wurde beendet."

