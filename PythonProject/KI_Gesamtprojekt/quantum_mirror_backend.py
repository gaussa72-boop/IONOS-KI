# quantum_mirror_backend.py - minimal backend engine for local testing

class QuantumMirrorBackend:
    def __init__(self):
        self.users = {}
        self.mirrors = {}
        self.games = {}
        self.chat_rooms = {"Wunderland": []}
        self.next_user_id = 1

    def register_user(self, username, email):
        user_id = self.next_user_id
        self.users[user_id] = {"username": username, "email": email}
        self.next_user_id += 1
        return {"id": user_id, "username": username, "email": email}

    def create_mirror(self, user_id, idea):
        mirror_id = f"mirror_{len(self.mirrors)+1}"
        self.mirrors[mirror_id] = {"user_id": user_id, "idea": idea}
        return {"mirror_id": mirror_id, "idea": idea}

    def break_mirror(self, mirror_id):
        if mirror_id not in self.mirrors:
            return {"error": "mirror not found"}
        self.mirrors[mirror_id]["broken"] = True
        return {"status": "broken", "mirror_id": mirror_id}

    def send_chat_message(self, user_id, room, message):
        if room not in self.chat_rooms:
            self.chat_rooms[room] = []
        self.chat_rooms[room].append({"user": user_id, "message": message})
        return {"status": "ok"}

    def get_user_avatar(self, user_id):
        user = self.users.get(user_id)
        if not user:
            return None
        return {"user": user_id, "avatar": {"name": user.get('username')}}

