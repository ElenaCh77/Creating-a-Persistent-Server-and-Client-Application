import socket

HOST = "0.0.0.0"
PORT = 50007
WELCOME_MSG = "Connected to the server! Welcome.\n"
FILE_PATH = "message.txt"

def main():
   
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write("There is a pop quiz coming soon")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT} ...")

        while True:
            conn, addr = s.accept()
            print(f"New client connected: {addr}")
            with conn:
                try:
                    # 1) Send welcome message
                    conn.sendall(WELCOME_MSG.encode("utf-8"))

                    # 2) Send the text file (small file, simple send)
                    with open(FILE_PATH, "rb") as f:
                        data = f.read()
                        conn.sendall(data)

                    print(f"Sent file {FILE_PATH} ({len(data)} bytes)")
                except Exception as e:
                    print("Error:", e)

if __name__ == "__main__":
    main()