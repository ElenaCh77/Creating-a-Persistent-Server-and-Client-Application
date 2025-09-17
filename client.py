import socket
import tkinter as tk
from tkinter import messagebox

SERVER_IP = "127.0.0.1"
PORT = 50007
OUT_FILE = "received_message.txt"

def show_popup(msg: str):
   
    root = tk.Tk()
    root.title("Client")
    root.geometry("260x100")  
    root.resizable(False, False)

    # show popup 
    root.after(100, lambda: messagebox.showinfo("Server Message", msg))

    # Quit button 
    tk.Label(root, text="Welcome received.\nFile will be saved next.").pack(pady=8)
    tk.Button(root, text="Quit", command=root.destroy).pack(pady=4)

    root.mainloop()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))

        #  welcome message
        welcome = s.recv(128).decode("utf-8").strip()
        print("Server says:", welcome)

        # show popup 
        show_popup(welcome)

        #  receive the file 
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
