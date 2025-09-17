import socket
import tkinter as tk
from tkinter import messagebox

SERVER_IP = "127.0.0.1"
PORT = 50007
OUT_FILE = "received_message.txt"

def show_popup(msg: str):
    # create a visible window (not hidden) so Windows focuses it
    root = tk.Tk()
    root.title("Client")
    root.geometry("260x100")  # small window so it’s obvious
    root.resizable(False, False)

    # show popup immediately after the window appears
    root.after(100, lambda: messagebox.showinfo("Server Message", msg))

    # simple label and Quit button so the app stays alive
    tk.Label(root, text="Welcome received.\nFile will be saved next.").pack(pady=8)
    tk.Button(root, text="Quit", command=root.destroy).pack(pady=4)

    root.mainloop()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))

        # 1) welcome message
        welcome = s.recv(128).decode("utf-8").strip()
        print("Server says:", welcome)

        # show popup (and keep a small window so it can’t hide behind)
        show_popup(welcome)

        # 2) receive the file (read until server closes)
        chunks = []
        while True:
            part = s.recv(4096)
            if not part:
                break
            chunks.append(part)
        data = b"".join(chunks)

        with open(OUT_FILE, "wb") as f:
            f.write(data)

        print(f"Saved file as {OUT_FILE}")

if __name__ == "__main__":
    main()