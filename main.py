import customtkinter as ctk
from PIL import Image
import os
import sys
import threading

def resource_path(relative_path):
    """ Findet Ressourcen im Bundle oder im lokalen Ordner """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MirrorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quantum Mirror Portal")
        self.geometry("1100x700")

        # Hintergrund laden
        try:
            bg_p = resource_path("Bilder.KI/189C2620-7E6C-4A58-9659-465F84F937AB.jpg")
            self.bg_image = ctk.CTkImage(Image.open(bg_p), size=(1100, 700))
            self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
            self.bg_label.place(x=0, y=0)
        except:
            print("Hintergrund konnte nicht geladen werden.")

        self.label = ctk.CTkLabel(self, text="QUANTUM MIRROR PORTAL", font=("Courier", 40, "bold"), text_color="#00FFFF")
        self.label.pack(pady=40)

        self.scroll_frame = ctk.CTkScrollableFrame(self, orientation="horizontal", fg_color="transparent", height=400)
        self.scroll_frame.pack(fill="x", padx=30)

        # WICHTIG: Hier müssen die Namen deiner .py Dateien im Hauptordner stehen!
        self.portals = [
            {"name": "Quantum AI", "img": "Bilder.KI/1.jpg.jpg", "script": "main.py"}, 
            {"name": "IONOS KI", "img": "Bilder.KI/2.jpg.jpg", "script": "app.py"},
            {"name": "Ultra KI", "img": "Bilder.KI/4.jpg.jpg", "script": "ultra_superki.py"}
        ]
        self.load_portals()

    def load_portals(self):
        for p in self.portals:
            try:
                img_p = resource_path(p["img"])
                img = ctk.CTkImage(Image.open(img_p), size=(200, 300))
                btn = ctk.CTkButton(self.scroll_frame, image=img, text=p["name"], compound="top",
                                    fg_color="transparent", hover_color="#1f538d",
                                    command=lambda x=p: self.shatter(x))
                btn.pack(side="left", padx=20)
            except:
                print(f"Bild {p['img']} fehlt.")

    def shatter(self, portal):
        print(f"💥 ZERBRUCH: {portal['name']}")
        # Visueller Effekt
        orig = self.cget("fg_color")
        self.configure(fg_color="white")
        self.after(100, lambda: self.configure(fg_color=orig))
        # Startet das Skript im Hintergrund
        script_path = os.path.join(os.getcwd(), portal["script"])
        threading.Thread(target=lambda: os.system(f"python3 {script_path}")).start()

if __name__ == "__main__":
    app = MirrorApp()
    app.mainloop()
