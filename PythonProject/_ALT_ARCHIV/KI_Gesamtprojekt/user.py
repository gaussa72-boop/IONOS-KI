from ..database import db
from datetime import datetime
import bcrypt


class User(db.Model):
    """User Model"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    profile = db.relationship("Profile", backref="user", uselist=False, cascade="all, delete-orphan")
    training_data = db.relationship("TrainingData", backref="user", cascade="all, delete-orphan")
    generated_games = db.relationship("GeneratedGame", backref="user", cascade="all, delete-orphan")

    def set_password(self, raw_password):
        """Hash and set password"""
        self.password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, raw_password):
        """Verify password"""
        return bcrypt.checkpw(raw_password.encode("utf-8"), self.password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }
