#!/bin/bash

# Quantum Meta Core Setup Script for Linux (Ubuntu/Debian)
# Run: sudo bash install/install_linux.sh

echo "🚀 Quantum Meta Core - Linux Installation"
echo "=========================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then
   echo "❌ This script must be run as root (use sudo)"
   exit 1
fi

# Update system
echo "📦 Updating system packages..."
apt-get update
apt-get upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
echo "🐳 Installing Docker Compose..."
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Add current user to docker group
echo "👤 Adding user to docker group..."
usermod -aG docker $SUDO_USER

# Create directories
echo "📁 Creating directories..."
mkdir -p /opt/quantum-meta-core
mkdir -p /opt/quantum-meta-core/generated_games

# Copy files (assuming run from project directory)
echo "📋 Setting up project files..."
cd /opt/quantum-meta-core

# Start services
echo "🚀 Starting Docker containers..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Check health
echo "🏥 Checking health status..."
curl http://localhost:5000/health

echo ""
echo "✅ Installation complete!"
echo "=========================================="
echo "🌐 Access the application at: http://localhost"
echo "📊 API Documentation: http://localhost/api"
echo ""
echo "Next steps:"
echo "1. Copy .env.example to .env and configure"
echo "2. Set up SSL with: sudo bash cloud/ssl/certbot-setup.sh"
echo "3. Configure domain in NGINX"
echo ""
echo "Command reference:"
echo "  docker-compose logs -f          # View logs"
echo "  docker-compose down             # Stop services"
echo "  docker-compose restart          # Restart services"

