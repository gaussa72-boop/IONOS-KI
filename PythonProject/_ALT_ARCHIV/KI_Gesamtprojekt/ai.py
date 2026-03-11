"""
AI Routes
KI-Core Kommunikation
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..core.ai_core import create_ai_core
from ..core.training_engine import create_training_engine
from ..models.user import User
from ..database import db

ai_bp = Blueprint("ai", __name__, url_prefix="/api/ai")

ai_core = create_ai_core()
training_engine = create_training_engine(db)


@ai_bp.route("/process", methods=["POST"])
@jwt_required()
def process():
    """Process user input through AI"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # Get user profile
        profile = user.profile.to_dict() if user.profile else {}

        # Process through AI
        response = ai_core.process(prompt, profile)

        # Store training data
        training_engine.store_interaction(
            user_id=user_id,
            input_text=prompt,
            response=response["response"],
            module="ai_core",
            tone=profile.get("tone", "neutral")
        )

        # Update interaction count
        if user.profile:
            user.profile.interaction_count += 1
            db.session.commit()

        return jsonify({
            "success": True,
            "response": response["response"],
            "model": response["model"],
            "metadata": {
                "profile_applied": response["profile_applied"],
                "interaction_count": user.profile.interaction_count if user.profile else 0
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ai_bp.route("/models", methods=["GET"])
def get_models():
    """Get available AI models"""
    return jsonify({
        "available_models": [
            {
                "name": "Quantum-LLM-Core-1.0",
                "description": "Internal Quantum Meta Core LLM",
                "status": "active"
            },
            {
                "name": "gpt-4",
                "description": "OpenAI GPT-4 (optional integration)",
                "status": "available"
            },
            {
                "name": "claude-3",
                "description": "Anthropic Claude (optional integration)",
                "status": "available"
            }
        ]
    }), 200


@ai_bp.route("/integrate_external", methods=["POST"])
@jwt_required()
def integrate_external():
    """Integrate external LLM API"""
    try:
        data = request.get_json()
        api_key = data.get("api_key")
        model = data.get("model", "gpt-4")

        result = ai_core.integrate_external_llm(api_key, model)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
