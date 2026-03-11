from ..database import db
from datetime import datetime


class TrainingData(db.Model):
    """Training Data for KI Evolution"""
    __tablename__ = "training_data"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    input_text = db.Column(db.Text, nullable=False)
    response_text = db.Column(db.Text, nullable=False)

    # Metadata
    module = db.Column(db.String(50))  # ai_core, game_creator, etc.
    tone_applied = db.Column(db.String(50))
    success = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "input": self.input_text,
            "response": self.response_text,
            "module": self.module,
            "created_at": self.created_at.isoformat()
        }
