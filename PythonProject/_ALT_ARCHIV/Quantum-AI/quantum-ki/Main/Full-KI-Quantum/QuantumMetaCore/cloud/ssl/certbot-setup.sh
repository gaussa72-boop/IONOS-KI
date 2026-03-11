#!/bin/bash

# SSL Certificate Setup with Let's Encrypt Certbot
# Run: sudo bash cloud/ssl/certbot-setup.sh

echo "🔒 SSL Certificate Setup with Let's Encrypt"
echo "=========================================="

if [ "$EUID" -ne 0 ]; then
   echo "❌ This script must be run as root"
   exit 1
fi

# Read domain
read -p "Enter your domain (e.g., quantummeta.example.com): " DOMAIN

if [ -z "$DOMAIN" ]; then
    echo "❌ Domain is required"
    exit 1
fi

# Install Certbot
echo "📦 Installing Certbot..."
apt-get install -y certbot python3-certbot-nginx

# Create certificates
echo "🔐 Creating SSL certificates..."
certbot certonly --standalone \
    -d $DOMAIN \
    --non-interactive \
    --agree-tos \
    -m admin@$DOMAIN

if [ $? -eq 0 ]; then
    # Copy certificates to nginx directory
    echo "📋 Copying certificates..."
    CERT_PATH="/etc/letsencrypt/live/$DOMAIN"
    SSL_DIR="./cloud/ssl"

    mkdir -p $SSL_DIR
    cp $CERT_PATH/fullchain.pem $SSL_DIR/cert.pem
    cp $CERT_PATH/privkey.pem $SSL_DIR/key.pem

    # Update nginx.conf (uncomment HTTPS section)
    echo "✅ SSL certificates installed at $SSL_DIR"
    echo ""
    echo "Next steps:"
    echo "1. Uncomment the HTTPS section in cloud/nginx/nginx.conf"
    echo "2. Update server_name to: $DOMAIN"
    echo "3. Restart NGINX: docker-compose restart nginx"
    echo ""
    echo "Auto-renewal with cron:"
    echo "0 3 * * * certbot renew --quiet && cp /etc/letsencrypt/live/$DOMAIN/* ./cloud/ssl/"
else
    echo "❌ Failed to create certificates"
    exit 1
fi

