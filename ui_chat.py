import tkinter as tk
from ai_core import ai_response
from social_media import post_social

def open_chat_window():

    chat = tk.Toplevel()
    chat.title("Universal KI Chat")
    chat.geometry("700x600")
    chat.configure(bg="#0b0b1a")

    output = tk.Text(chat, bg="black", fg="white")
    output.pack(expand=True, fill="both")

    entry = tk.Entry(chat, bg="#222", fg="white")
    entry.pack(fill="x")

    def send():
        msg = entry.get()
        entry.delete(0, tk.END)

        output.insert(tk.END, "Du: " + msg + "\n")

        response = ai_response(msg)
        output.insert(tk.END, "KI: " + response + "\n")

    send_btn = tk.Button(chat, text="Senden", command=send)
    send_btn.pack()

    social_btn = tk.Button(
        chat,
        text="Poste Social Media",
        command=lambda: post_social("Automatischer KI Post")
    )
    social_btn.pack()