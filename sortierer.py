import os
import shutil
from pathlib import Path

# Pfad anpassen basierend auf deinem Screenshot-Verzeichnis
SOURCE_DIR = Path("./")
TARGET_DIR = Path("./MEGA_AGENT_WORKSPACE/app")

# Zuordnung von Schlüsselwörtern im Dateinamen zu den 10 Agenten
AGENT_MAPPING = {
    "agent_1": ["galactic", "engine"],
    "agent_2": ["quantum_ai", "metacore", "quantum-ai"],
    "agent_3": ["webapp", "mirror", "wonderland"],
    "agent_4": ["ionos"],
    "agent_5": ["ultra", "level23", "superki"],
    "agent_6": ["urspirit", "bilder", "spirit"],
    "agent_7": ["chat", "character"],
    "agent_8": ["tool", "helper", "utils"],
    "agent_9": ["fortschritt", "rea", "projekt"],
    "agent_10": ["quantum-ki", "quantumki"]
}


def intelligent_sort():
    for root, _, files in os.walk(SOURCE_DIR):
        # Vermeide es, den Zielordner rekursiv selbst zu scannen
        if "MEGA_AGENT_WORKSPACE" in root:
            continue

        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                file_path = Path(root) / file
                moved = False

                # Datei anhand des Namens oder des Ordnernamens zuordnen
                combined_path_string = (str(file_path) + file).lower()

                for agent_folder, keywords in AGENT_MAPPING.items():
                    if any(keyword in combined_path_string for keyword in keywords):
                        shutil.copy(file_path, TARGET_DIR / agent_folder / file)
                        print(f"-> Zugeordnet zu {agent_folder}: {file}")
                        moved = True
                        break

                if not moved:
                    # Wenn nichts greift, ab in den allgemeinen Core-Ordner
                    shutil.copy(file_path, TARGET_DIR / "core" / file)


if __name__ == "__main__":
    intelligent_sort()
    print("\n--- Alle brauchbaren Kodes wurden in die 10 Agenten-Ordner sortiert! ---")