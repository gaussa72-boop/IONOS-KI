# 🌀 QUANTUM META CORE - QUICK REFERENCE GUIDE

## Startup Commands

### Option 1: Docker (RECOMMENDED)
```bash
cd /Users/Querox9396/PycharmProjects/QuantumMetaCore
docker-compose up -d
curl http://localhost/health
```

### Option 2: Local Python
```bash
cd /Users/Querox9396/PycharmProjects/QuantumMetaCore
pip install -r requirements.txt
python wsgi.py
# Access: http://localhost:5000
```

### Option 3: Automatic macOS Setup
```bash
bash /Users/Querox9396/PycharmProjects/QuantumMetaCore/install/install_mac.sh
```

---

## Common Commands

### Docker
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f backend
docker-compose logs -f postgres

# Restart a service
docker-compose restart backend

# Execute command in container
docker-compose exec backend python
```

### Database
```bash
# Access PostgreSQL
docker-compose exec postgres psql -U quantum_user -d quantum_db

# Check Redis
docker-compose exec redis redis-cli ping
```

### Development
```bash
# Run tests
pytest

# Code coverage
pytest --cov=app

# Linting
flake8 app
black app
```

---

## API Quick Test

### 1. Register User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
  }'
```

### 2. Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### 3. Use AI Core
```bash
TOKEN="your_jwt_token_here"

curl -X POST http://localhost:5000/api/ai/process \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Was ist eine Singularität?"
  }'
```

### 4. Create Game
```bash
curl -X POST http://localhost:5000/api/game/create \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "Ein platformer Spiel",
    "genre": "platformer"
  }'
```

### 5. Get Profile
```bash
curl http://localhost:5000/api/profile/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## Configuration

### Environment Variables
Copy `.env.example` to `.env` and configure:

```env
FLASK_ENV=development
DATABASE_URL=sqlite:///quantum_dev.db
REDIS_URL=redis://localhost:6379/0
```

### Production Environment
Use `cloud/production.env` for production deployment:

```env
FLASK_ENV=production
DATABASE_URL=postgresql://quantum_user:securepassword@postgres:5432/quantum_db
REDIS_URL=redis://redis:6379/0
```

---

## Project Structure
```
QuantumMetaCore/
├── app/                    # Flask Application
│   ├── models/            # Database Models
│   ├── core/              # Core Engines
│   └── routes/            # API Endpoints
├── config.py              # Configuration
├── wsgi.py                # Entry Point
├── Dockerfile             # Container
├── docker-compose.yml     # Multi-container
├── requirements.txt       # Dependencies
└── install/               # Installation Scripts
```

---

## Database Models

### Users
- id, username, email, password, created_at

### Profiles
- id, user_id, tone, depth, level, interaction_count

### Training Data
- id, user_id, input_text, response_text, module, created_at

### Generated Games
- id, user_id, game_id, idea, genre, plays, rating

---

## Deployment

### Render.com
1. Connect GitHub repository
2. Choose Python environment
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn wsgi:app`

### IONOS vServer
```bash
sudo bash install/install_linux.sh
```

### Custom Server
```bash
# Copy files to server
scp -r QuantumMetaCore/ user@server:/opt/

# Setup SSL
sudo bash cloud/ssl/certbot-setup.sh

# Start services
docker-compose up -d
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process on port 5000
lsof -i :5000
# Kill it
kill -9 <PID>
```

### Database Connection Error
```bash
# Check PostgreSQL
docker-compose logs postgres

# Rebuild database
docker-compose down -v
docker-compose up -d
```

### Redis Connection Error
```bash
# Check Redis
docker-compose exec redis redis-cli ping

# Restart Redis
docker-compose restart redis
```

---

## Performance Tuning

### Database
- Add indexes on frequently queried fields
- Use connection pooling
- Monitor query performance

### Caching
- Configure Redis TTL
- Implement cache warmup
- Monitor cache hit rate

### Web Server
- Adjust Gunicorn worker count
- Configure NGINX caching
- Enable gzip compression

---

## Security

### SSL/TLS Setup
```bash
sudo bash cloud/ssl/certbot-setup.sh
```

### Update Dependencies
```bash
pip install -r requirements.txt --upgrade
docker-compose pull
```

### Backup Database
```bash
docker-compose exec postgres pg_dump -U quantum_user quantum_db > backup.sql
```

---

## Monitoring

### Health Check
```bash
curl http://localhost:5000/health
```

### Logs
```bash
docker-compose logs -f
```

### Metrics
- Database connections
- Cache hit rate
- API response time
- Error rates

---

## Development Tips

### Database Migrations
```bash
flask db init
flask db migrate -m "message"
flask db upgrade
```

### Testing
```bash
pytest -v
pytest --cov=app --cov-report=html
```

### Code Quality
```bash
flake8 app
black app
pylint app
```

---

## Useful Links

- **Documentation**: README.md
- **API Docs**: http://localhost:5000/
- **Status**: http://localhost:5000/health
- **GitHub**: (Configure in repository)

---

**Last Updated**: March 4, 2026  
**Version**: 1.0.0  
**Status**: Production Ready

