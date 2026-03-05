#!/bin/bash

# Quantum Meta Core Setup Script for macOS
# Run: bash install/install_mac.sh

echo "🚀 Quantum Meta Core - macOS Installation"
echo "=========================================="

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "📦 Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Docker Desktop (manual or via brew)
echo "🐳 Installing Docker..."
if ! command -v docker &> /dev/null; then
    echo "Please install Docker Desktop from https://www.docker.com/products/docker-desktop"
    echo "Or run: brew install docker"
    exit 1
fi

# Install Docker Compose (usually comes with Docker Desktop)
if ! command -v docker-compose &> /dev/null; then
    echo "🐳 Installing Docker Compose..."
    brew install docker-compose
fi

# Install Python (optional, for local development)
echo "🐍 Installing Python..."
brew install python@3.11

# Create project directory
echo "📁 Creating project directory..."
mkdir -p ~/quantum-meta-core
cd ~/quantum-meta-core

# Copy .env
echo "⚙️  Setting up environment..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "⚠️  Please edit .env with your configuration"
fi

# Create directories
mkdir -p generated_games
mkdir -p cloud/ssl

# Start services
echo "🚀 Starting Docker containers..."
docker-compose up -d

# Wait for services
echo "⏳ Waiting for services to start..."
sleep 10

# Check health
echo "🏥 Checking health status..."
curl http://localhost:5000/health

echo ""
echo "✅ Installation complete!"
echo "=========================================="
echo "🌐 Access the application at: http://localhost"
echo "📊 API available at: http://localhost/api"
echo ""
echo "Useful commands:"
echo "  docker-compose logs -f          # View logs"
echo "  docker-compose ps               # Show containers"
echo "  docker-compose stop             # Stop services"
echo "  docker-compose down             # Stop and remove"
echo ""
echo "Development with local Python:"
echo "  python3 -m venv venv"
echo "  source venv/bin/activate"
echo "  pip install -r requirements.txt"
echo "  python wsgi.py"

