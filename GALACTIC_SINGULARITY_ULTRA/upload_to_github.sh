#!/bin/bash
# 🌌 GALACTIC SINGULARITY - QUICK GITHUB UPLOAD
# =============================================

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║    🌌 GALACTIC SINGULARITY - GITHUB UPLOAD SCRIPT 🌌         ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Frage nach GitHub URL
echo "📝 GitHub Repository URL eingeben:"
echo "   Format: https://github.com/DEINNAME/galactic-singularity-ultra.git"
echo ""
read -p "🔗 Repository URL: " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "❌ Keine URL eingegeben!"
    exit 1
fi

cd /Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA

echo ""
echo "📦 Schritt 1: Git initialisieren..."
git init

echo ""
echo "📦 Schritt 2: .gitignore prüfen..."
if [ -f ".gitignore" ]; then
    echo "✓ .gitignore existiert"
else
    echo "✗ .gitignore wird erstellt..."
    cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
env/
venv/
.DS_Store
.env
galactic_singularity.db
*.log
EOF
fi

echo ""
echo "📦 Schritt 3: Alle Dateien hinzufügen..."
git add .
echo "✓ Dateien hinzugefügt"

echo ""
echo "📦 Schritt 4: Erster Commit..."
git commit -m "🌌 Initial commit: Galactic Singularity ULTRA 2.0 - Complete AI System with Galactic Portal"

echo ""
echo "📦 Schritt 5: Remote Repository hinzufügen..."
git remote add origin "$REPO_URL"
echo "✓ Remote hinzugefügt"

echo ""
echo "📦 Schritt 6: Branch umbenennen zu 'main'..."
git branch -M main

echo ""
echo "📦 Schritt 7: Hochladen zu GitHub..."
echo "   (Du wirst nach GitHub Credentials gefragt)"
echo ""
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "════════════════════════════════════════════════════════════════"
    echo "✨ ERFOLGREICH HOCHGELADEN! ✨"
    echo "════════════════════════════════════════════════════════════════"
    echo ""
    echo "📖 Repository: $REPO_URL"
    echo ""
    echo "✓ Dein Projekt ist jetzt auf GitHub!"
    echo "✓ URL: https://github.com/DEINNAME/galactic-singularity-ultra"
    echo ""
else
    echo ""
    echo "❌ Fehler beim Upload!"
    echo "Überprüfe deine GitHub Credentials und versuche es erneut."
fi

echo ""
echo "🌌 Viel Erfolg mit deinem Projekt! ✨"

