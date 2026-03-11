from ..database import db
from datetime import datetime
import my_json


class GeneratedGame(db.Model):
    """Generated Game Model"""
    __tablename__ = "generated_games"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    game_id = db.Column(db.String(100), unique=True, nullable=False)
    idea = db.Column(db.Text, nullable=False)

    # Game attributes
    genre = db.Column(db.String(50))  # RPG, Puzzle, Adventure, etc.
    game_type = db.Column(db.String(50))  # webgl, html, unity_project
    description = db.Column(db.Text)

    # Metadata
    file_path = db.Column(db.String(200))
    status = db.Column(db.String(20), default="active")  # active, archived, draft
    plays = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "game_id": self.game_id,
            "idea": self.idea,
            "genre": self.genre,
            "game_type": self.game_type,
            "plays": self.plays,
            "rating": self.rating,
            "created_at": self.created_at.isoformat()
        }
