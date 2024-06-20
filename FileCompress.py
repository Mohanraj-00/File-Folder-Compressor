import tkinter as tk
from tkinter import filedialog, messagebox
import zlib
import os
import shutil

class FileCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor")
        self.root.geometry("500x300")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="File and Folder Compressor", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.compress_file_button = tk.Button(self.root, text="Compress File", command=self.compress_file)
        self.compress_file_button.pack(pady=5)

        self.decompress_file_button = tk.Button(self.root, text="Decompress File", command=self.decompress_file)
        self.decompress_file_button.pack(pady=5)

        self.compress_folder_button = tk.Button(self.root, text="Compress Folder", command=self.compress_folder)
        self.compress_folder_button.pack(pady=5)

        self.decompress_folder_button = tk.Button(self.root, text="Decompress Folder", command=self.decompress_folder)
        self.decompress_folder_button.pack(pady=5)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

    def update_status(self, message):
        self.status_label.config(text=message)

    def compress_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'rb') as input_file:
                    data = input_file.read()
                    compressed_data = zlib.compress(data)
                    output_file_path = file_path + '.zlib'
                    with open(output_file_path, 'wb') as output_file:
                        output_file.write(compressed_data)
                    self.update_status(f"Compressed file saved as {output_file_path}")
            except Exception as e:
                self.update_status(f"Failed to compress file: {e}")

    def decompress_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'rb') as input_file:
                    compressed_data = input_file.read()
                    decompressed_data = zlib.decompress(compressed_data)
                    output_file_path = file_path.replace('.zlib', '_decompressed')
                    with open(output_file_path, 'wb') as output_file:
                        output_file.write(decompressed_data)
                    self.update_status(f"Decompressed file saved as {output_file_path}")
            except Exception as e:
                self.update_status(f"Failed to decompress file: {e}")

    def compress_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            output_file_path = folder_path + '.zip'
            try:
                shutil.make_archive(folder_path, 'zip', folder_path)
                self.update_status(f"Compressed folder saved as {output_file_path}")
            except Exception as e:
                self.update_status(f"Failed to compress folder: {e}")

    def decompress_folder(self):
        file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        if file_path:
            output_folder_path = file_path.replace('.zip', '_decompressed')
            try:
                shutil.unpack_archive(file_path, output_folder_path, 'zip')
                self.update_status(f"Decompressed folder saved at {output_folder_path}")
            except Exception as e:
                self.update_status(f"Failed to decompress folder: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileCompressorApp(root)
    root.mainloop()
