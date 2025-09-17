# Creating a Persistent Server and Client Application

## 🎯 Objective
The goal of this assignment is to develop a client–server application using Python sockets.

- The **server** continuously listens for incoming client connections.
- Each time a client connects:
  - The server displays a message in the terminal.
  - The server sends a **welcome message** and a **text file**.
- The **client**:
  - Connects to the server.
  - Shows the welcome message in a **popup window**.
  - Saves the received text file locally.

---

## 📂 Project Structure

Creating-a-Persistent-Server-and-Client-Application/
│── server.py # Server code
│── client.py # Client code
│── README.md # Instructions and documentation

yaml
Copy code

> Note:  
> - `message.txt` is created automatically by the server.  
> - `received_message.txt` is created automatically by the client.  

---

## ⚙️ Requirements
- Python 3 (from [python.org](https://www.python.org/downloads/))
- Tkinter (comes included with Python on Windows/macOS)

---

## 🚀 How to Run

### 1. Start the Server
Open a terminal in the project folder and run:
```bash
py server.py
Output example:

nginx
Copy code
Server listening on 0.0.0.0:50007 ...
New client connected: ('127.0.0.1', 54321)
Sent file message.txt (30 bytes)
2. Run the Client
In another terminal (or another computer on the same network):

bash
Copy code
py client.py
A popup window will appear with:
“Connected to the server! Welcome.”

The client saves the received file as received_message.txt.

3. View the Received File
In PowerShell:

powershell
Copy code
cat .\received_message.txt
In Command Prompt:

cmd
Copy code
type received_message.txt
Output:

csharp
Copy code
There is a pop quiz coming soon

Output:

There is a pop quiz coming soon
