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
