import tkinter as tk
from ui_chat import open_chat_window

def open_ai():
    open_chat_window()

root = tk.Tk()
root.title("Social Media KI Plattform")
root.geometry("500x400")
root.configure(bg="black")

title = tk.Label(
    root,
    text="Social Media Quanten KI",
    fg="gold",
    bg="black",
    font=("Arial", 20)
)
title.pack(pady=20)

open_button = tk.Button(
    root,
    text="KI Plattform öffnen",
    command=open_ai,
    font=("Arial", 14),
    bg="purple",
    fg="white"
)
open_button.pack(pady=20)

root.mainloop()
from automation.system_loop import run_system

if __name__ == "__main__":

    print("🚀 AI AUTONOMY PLATFORM STARTED")

    while True:

        result = run_system()

        print("🤖 SYSTEM OUTPUT:", result)
        from automation.system_loop import run_system

        if __name__ == "__main__":

            print("🚀 AI SAAS PLATFORM STARTED (LEVEL 1-11+)")

            while True:
                result = run_system()

                print("🤖 AI OUTPUT:", result)
                from backend.server import app

                if __name__ == "__main__":
                    app.run(debug=True)