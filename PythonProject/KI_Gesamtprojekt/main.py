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
import argparse
import sys

import pbr._compat.metadata
import pbr.version


def get_sha(args):
    sha = _get_info(args.name)['sha']
    if sha:
        print(sha)


def get_info(args):
    if args.short:
        print("{version}".format(**_get_info(args.name)))
    else:
        print(
            "{name}\t{version}\t{released}\t{sha}".format(
                **_get_info(args.name)
            )
        )


def _get_info(package_name):
    metadata = pbr._compat.metadata.get_metadata(package_name)
    version = pbr._compat.metadata.get_version(package_name)

    if metadata:
        if metadata['is_release']:
            released = 'released'
        else:
            released = 'pre-release'
        sha = metadata['git_version']
    else:
        version_parts = version.split('.')
        if version_parts[-1].startswith('g'):
            sha = version_parts[-1][1:]
            released = 'pre-release'
        else:
            sha = ""
            released = "released"
            for part in version_parts:
                if not part.isdigit():
                    released = "pre-release"

    return {
        'name': package_name,
        'version': version,
        'sha': sha,
        'released': released,
    }


def freeze(args):
    for dist in pbr._compat.metadata.get_distributions():
        info = _get_info(dist.project_name)
        output = "{name}=={version}".format(**info)
        if info['sha']:
            output += "  # git sha {sha}".format(**info)
        print(output)


def main():
    parser = argparse.ArgumentParser(
        description='pbr: Python Build Reasonableness'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=str(pbr.version.VersionInfo('pbr')),
    )

    subparsers = parser.add_subparsers(
        title='commands',
        description='valid commands',
        help='additional help',
        dest='cmd',
    )
    subparsers.required = True

    cmd_sha = subparsers.add_parser('sha', help='print sha of package')
    cmd_sha.set_defaults(func=get_sha)
    cmd_sha.add_argument('name', help='package to print sha of')

    cmd_info = subparsers.add_parser(
        'info', help='print version info for package'
    )
    cmd_info.set_defaults(func=get_info)
    cmd_info.add_argument('name', help='package to print info of')
    cmd_info.add_argument(
        '-s',
        '--short',
        action="store_true",
        help='only display package version',
    )

    cmd_freeze = subparsers.add_parser(
        'freeze', help='print version info for all installed packages'
    )
    cmd_freeze.set_defaults(func=freeze)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sys.exit(main())
