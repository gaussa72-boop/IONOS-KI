from core.engine import start_singularity
from interfaces.chat_hub.app import launch_chat

def ignite_singularity():

    print("🌌 QUANTUM SINGULARITY WIRD ENTFACHT...")

    engine = start_singularity()

    launch_chat(engine)

if __name__ == "__main__":
    ignite_singularity()