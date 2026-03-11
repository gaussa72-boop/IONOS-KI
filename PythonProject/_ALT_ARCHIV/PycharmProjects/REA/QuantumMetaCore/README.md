# 🌀 Quantum Meta Core - Production Backend

**Version**: 1.0.0  
**Status**: Production Ready  
**Architecture**: Enterprise-Grade Modular Flask + PostgreSQL + Redis

---

## 🎯 Überblick

**Quantum Meta Core** ist eine zentrale KI-Plattform für:
- 🤖 Adaptive KI-Begleiter-Systeme
- 🎮 Automatische Game-Generierung
- 📚 Langfristiges KI-Training und Evolution
- 🎨 Personalisierte Persönlichkeitsprofile
- ☁️ Cloud-skalierbare Architektur

---

## 📂 Projektstruktur

```
QuantumMetaCore/
├── app/                              # Flask Application
│   ├── __init__.py                  # App Factory
│   ├── database.py                  # Database Setup
│   ├── models/                      # SQLAlchemy Models
│   │   ├── user.py                 # User Model
│   │   ├── profile.py              # Profile Model
│   │   ├── training_data.py        # Training Data Model
│   │   └── generated_game.py       # Game Model
│   ├── core/                        # Core Engines
│   │   ├── ai_core.py              # KI-Intelligenz
│   │   ├── companion_core.py       # KI-Begleiter
│   │   ├── game_generator_engine.py # Game-Generierung
│   │   ├── personality_engine.py   # Persönlichkeitsentwicklung
│   │   └── training_engine.py      # Training & Learning
│   └── routes/                      # API Endpoints
│       ├── auth.py                 # Authentication
│       ├── ai.py                   # KI API
│       ├── companion.py            # Companion API
│       ├── game.py                 # Game Creator API
│       └── profile.py              # Profile Management
├── generated_games/                 # Auto-generated Games
├── config.py                        # Configuration
├── wsgi.py                          # Production Entry Point
├── Dockerfile                       # Docker Container
├── docker-compose.yml              # Multi-Container Setup
├── requirements.txt                # Python Dependencies
└── install/                        # Installation Scripts
```

---

## 🚀 Quick Start

### Lokal (macOS/Linux)

```bash
# 1. Clone repository
cd QuantumMetaCore

# 2. Setup environment
cp .env.example .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run development server
python wsgi.py
```

### Mit Docker

```bash
# Starte alle Services
docker-compose up -d

# Überprüfe Status
docker-compose ps

# Logs anschauen
docker-compose logs -f backend
```

### Automatisches Setup

**macOS:**
```bash
bash install/install_mac.sh
```

**Linux:**
```bash
sudo bash install/install_linux.sh
```

---

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Registrierung
- `POST /api/auth/login` - Login
- `GET /api/auth/verify` - Token Verify

### KI-Core
- `POST /api/ai/process` - KI Verarbeitung
- `GET /api/ai/models` - Verfügbare Modelle

### Companion
- `POST /api/companion/speak` - Begleiter antwortet
- `GET /api/companion/status` - Begleiter-Status
- `PUT /api/companion/personality` - Persönlichkeit anpassen

### Game Creator
- `POST /api/game/create` - Game erzeugen
- `GET /api/game/list` - Games auflisten
- `POST /api/game/<id>/play` - Game spielen

### Profile Management
- `GET /api/profile/` - Profile abrufen
- `PUT /api/profile/update` - Profile aktualisieren
- `GET /api/profile/evolution` - Evolution-Status
- `GET /api/profile/stats` - Statistiken

---

## 🧠 Core Engines

### 1. AI Core
Zentrale KI-Intelligenz mit optionaler LLM-Integration

```python
POST /api/ai/process
{
  "prompt": "Was ist eine Singularität?",
  "context": "optional"
}
```

### 2. Companion Core
Personalisierter KI-Begleiter

```python
POST /api/companion/speak
{
  "message": "Hallo Begleiter!"
}
```

### 3. Game Generator Engine
Erzeugt spielbare Mini-Games aus Ideen

```python
POST /api/game/create
{
  "idea": "Ein Jump-and-Run Spiel",
  "genre": "puzzle"
}
```

### 4. Personality Engine
Verwaltet KI-Evolution (10 Stufen)

```
Level 1: Initiate
Level 2: Explorer
Level 3: Creator
Level 4: Master
...
Level 10: Quantum
```

### 5. Training Engine
Speichert Interaktionen für langfristiges Lernen

---

## ⚙️ Konfiguration

### Environment Variables

```env
# Flask
FLASK_ENV=production
FLASK_DEBUG=False

# Database
DATABASE_URL=postgresql://user:pass@host:5432/quantum_db

# Redis
REDIS_URL=redis://host:6379/0

# Security
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_key
```

### Production Setup

1. **PostgreSQL verwenden:**
   ```env
   DATABASE_URL=postgresql://quantum_user:securepassword@postgres:5432/quantum_db
   ```

2. **Redis cachen:**
   ```env
   REDIS_URL=redis://redis:6379/0
   ```

3. **SSL aktivieren:**
   ```bash
   sudo bash cloud/ssl/certbot-setup.sh
   ```

---

## 🐳 Docker Deployment

### Start Services
```bash
docker-compose up -d
```

### Stop Services
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f backend
docker-compose logs -f postgres
docker-compose logs -f redis
```

### Restart Service
```bash
docker-compose restart backend
```

---

## 📊 Datenbank-Schema

### Users
```sql
id | username | email | password | created_at
```

### Profiles
```sql
id | user_id | tone | depth | level | interaction_count
```

### Training Data
```sql
id | user_id | input_text | response_text | module | created_at
```

### Generated Games
```sql
id | user_id | game_id | idea | genre | plays | rating
```

---

## 🔒 Sicherheit

- ✅ **Password Hashing**: bcrypt
- ✅ **JWT Tokens**: Flask-JWT-Extended
- ✅ **CORS Protection**: Flask-CORS
- ✅ **SQL Injection Prevention**: SQLAlchemy ORM
- ✅ **SSL/TLS**: Let's Encrypt + Certbot

---

## 📈 Monitoring

### Health Check
```bash
curl http://localhost:5000/health
```

### Metrics
- API response time
- Database connection pool
- Redis memory usage
- Container resource usage

---

## 🚢 Deployment

### Render.com
1. Connect GitHub Repository
2. Select Python environment
3. Build: `pip install -r requirements.txt`
4. Start: `gunicorn wsgi:app`

### IONOS vServer
```bash
sudo bash install/install_linux.sh
```

### AWS / GCP / Azure
1. Docker Image pushen
2. Container Service deployen
3. Database konfigurieren
4. SSL Setup

---

## 🛠️ Development

### Testing
```bash
pytest
pytest --cov=app
```

### Linting
```bash
flake8 app
black app
```

### Database Migration
```bash
flask db init
flask db migrate
flask db upgrade
```

---

## 📚 Integration

### Unity Game Engine
```csharp
using UnityEngine;
using UnityEngine.Networking;

public class QuantumAPI : MonoBehaviour {
    IEnumerator CallAPI(string prompt) {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost/api/ai/process?prompt=" + prompt);
        yield return www.SendWebRequest();
        Debug.Log(www.downloadHandler.text);
    }
}
```

### Frontend Integration
```javascript
fetch('/api/ai/process', {
  method: 'POST',
  headers: {'Authorization': 'Bearer ' + token},
  body: JSON.stringify({prompt: 'Your question'})
})
.then(r => r.json())
.then(data => console.log(data.response))
```

---

## 📞 Support

**Issues:** GitHub Issues  
**Docs:** `/docs`  
**Status:** http://localhost/health  

---

## 📄 Lizenz

MIT License - © 2026 Quantum Meta Core

---

**🌀 Quantum Meta Core - Powering Adaptive AI Universes**

