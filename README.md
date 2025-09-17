
# Creating a Persistent Server and Client Application

This project was created as an assignment to demonstrate socket programming in Python.

## Objective
- The server continuously listens for incoming client connections.
- Each time a client connects, the server displays a message in the terminal.
- The server sends a welcome message and a text file to the client.
- The client displays the welcome message in a popup window and saves the text file locally.

## Files
- **server.py** – Python server that listens on port 50007, sends a welcome message and a text file.
- **client.py** – Python client that connects to the server, shows a popup with the welcome message, and saves the received text file as `received_message.txt`.

## How to Run
1. Start the server:
   ```bash
   py server.py


   Output:

Server listening on 0.0.0.0:50007 ...


2. Start the client (in a second terminal or on another computer):

py client.py


A popup window will show: “Connected to the server! Welcome.”

The file will be saved as received_message.txt.

3. View the file contents:

PowerShell:
cat .\received_message.txt


Command Prompt:
type received_message.txt


Output:

There is a pop quiz coming soon
