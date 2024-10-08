# Secure-file-transfer-Application-
Secure file transfer Application python 
import socket
import threading
import os

# Define the server's address and port
HOST = '0.0.0.0'
PORT = 5000
BUFFER_SIZE = 4096

# Directory to store uploaded files
UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            # Receive the command from the client
            command = conn.recv(BUFFER_SIZE).decode()
            if not command:
                break
            
            if command.startswith('UPLOAD'):
                filename = command.split()[1]
                with open(os.path.join(UPLOAD_DIR, filename), 'wb') as file:
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                            break
                        file.write(data)
                print(f"Received file: {filename}")
            elif command.startswith('DOWNLOAD'):
                filename = command.split()[1]
                if os.path.exists(os.path.join(UPLOAD_DIR, filename)):
                    conn.sendall(b'OK')
                    with open(os.path.join(UPLOAD_DIR, filename), 'rb') as file:
                        while (data := file.read(BUFFER_SIZE)):
                            conn.sendall(data)
                else:
                    conn.sendall(b'File not found')
            else:
                conn.sendall(b'Invalid command')
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()




.....
.....
.....
......
........
        2nd code 

        import socket

import tkinter as tk

from tkinter import filedialog

from tkinter import messagebox



HOST = 'localhost'

PORT = 5000

BUFFER_SIZE = 4096



def upload_file():

    filename = filedialog.askopenfilename()

    if not filename:

        return



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        s.sendall(f"UPLOAD {filename}".encode())

        with open(filename, 'rb') as file:

            while (data := file.read(BUFFER_SIZE)):

                s.sendall(data)

        messagebox.showinfo("Info", "File uploaded successfully")



def download_file():

    filename = filedialog.asksaveasfilename()

    if not filename:

        return



    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        s.sendall(f"DOWNLOAD {filename}".encode())

        response = s.recv(BUFFER_SIZE).decode()

        if response == 'OK':

            with open(filename, 'wb') as file:

                while (data := s.recv(BUFFER_SIZE)):

                    if not data:

                        break

                    file.write(data)

            messagebox.showinfo("Info", "File downloaded successfully")

        else:

            messagebox.showerror("Error", "File not found on server")



app = tk.Tk()

app.title("File Sharing App")



upload_button = tk.Button(app, text="Upload File", command=upload_file)

upload_button.pack(pady=10)



download_button = tk.Button(app, text="Download File", command=download_file)

download_button.pack(pady=10)



app.mainloop()

