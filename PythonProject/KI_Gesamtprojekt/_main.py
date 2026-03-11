from warnings import warn

from .cli import *  # NOQA
from .cli import __all__  # NOQA
from .std import TqdmDeprecationWarning
import customtkinter as ctk
from PIL import Image
import os
import sys
import pygame
import threading


# --- Pfad-Finder für Mac & PyInstaller ---
def resource_path(relative_path):
     """ Findet Dateien (Bilder/Sounds) egal ob im Editor oder als fertige App """
     try:
          base_path = sys._MEIPASS
     except Exception:
          base_path = os.path.abspath(".")
     return os.path.join(base_path, relative_path)


class MirrorApp(ctk.CTk):
     def __init__(self):
          super().__init__()

          # Fenster Konfiguration
          self.title("Quantum Mirror Portal")
          self.geometry("1100x700")

          # Audio System
          pygame.mixer.init()

          # Hintergrund setzen (Bild 189C...)
          try:
               bg_path = resource_path("Bilder.KI/189C2620-7E6C-4A58-9659-465F84F937AB.jpg")
               self.bg_image = ctk.CTkImage(Image.open(bg_path), size=(1100, 700))
               self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
               self.bg_label.place(x=0, y=0)
          except:
               print("Hintergrundbild nicht gefunden.")

          # Überschrift
          self.label = ctk.CTkLabel(self, text="QUANTUM MIRROR WONDERLAND",
                                    font=("Courier New", 40, "bold"), text_color="#00FFFF")
          self.label.pack(pady=40)

          # Scrollbarer Bereich für die Spiegel-Portale
          self.scroll_frame = ctk.CTkScrollableFrame(self, orientation="horizontal",
                                                     fg_color="transparent", height=400)
          self.scroll_frame.pack(fill="x", padx=30)

          # Liste deiner Programme (Pfade zu deinen Bildern & Skripten)
          self.portals = [
               {"name": "Quantum AI", "img": "Bilder.KI/1.jpg.jpg", "script": "quantum_ai.py"},
               {"name": "IONOS KI", "img": "Bilder.KI/2.jpg.jpg", "script": "app.py"},
               {"name": "Ultra SuperKI", "img": "Bilder.KI/4.jpg.jpg", "script": "ultra_superki.py"},
               {"name": "MetaCore", "img": "Bilder.KI/5.jpg.jpg", "script": "metacore.py"},
               {"name": "System 7", "img": "Bilder.KI/7.jpg.jpg", "script": "script_7.py"}
          ]

          self.load_portals()

     def load_portals(self):
          for portal in self.portals:
               try:
                    img_path = resource_path(portal["img"])
                    img = ctk.CTkImage(Image.open(img_path), size=(200, 300))

                    btn = ctk.CTkButton(self.scroll_frame, image=img, text=portal["name"],
                                        compound="top", fg_color="transparent",
                                        hover_color="#1f538d", font=("Arial", 16, "bold"),
                                        command=lambda p=portal: self.shatter_mirror(p))
                    btn.pack(side="left", padx=20)
               except:
                    print(f"Konnte Bild {portal['img']} nicht laden.")

     def shatter_mirror(self, portal):
          # 1. Sound-Effekt (System Beep oder Datei)
          print(f"💥 SPIEGEL ZERBRICHT: {portal['name']} 💥")

          # 2. Kurzer Glitch-Effekt (Fenster flackert weiß)
          original_bg = self.cget("fg_color")
          self.configure(fg_color="white")
          self.after(100, lambda: self.configure(fg_color=original_bg))

          # 3. Programm im Hintergrund starten
          script_to_run = portal["script"]
          threading.Thread(target=lambda: os.system(f"python3 {script_to_run}")).start()


if __name__ == "__main__":
     app = MirrorApp()
     app.mainloop()
