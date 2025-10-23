import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(folder_path):
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.csv', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Code': ['.py', '.ipynb', '.env']
    }

    file_count = 0

    # Create folders if not exist
    for folder in extensions.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, exts in extensions.items():
                if ext in exts:
                    shutil.move(file_path, os.path.join(folder_path, folder, filename))
                    moved = True
                    file_count += 1
                    break
            if not moved:
                os.makedirs(os.path.join(folder_path, 'Others'), exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, 'Others', filename))
                file_count += 1

    return file_count

# GUI app
def choose_folder():
    folder_path = filedialog.askdirectory(title="Select Folder to Organize")
    if folder_path:
        count = organize_files(folder_path)
        messagebox.showinfo("Success", f"Organized {count} files successfully!")

# Tkinter window
root = tk.Tk()
root.title("File Organizer by Shameer")
root.geometry("400x200")

label = tk.Label(root, text="Click below to select a folder to organize", font=("Arial", 11))
label.pack(pady=20)

btn = tk.Button(root, text="Select Folder", command=choose_folder, bg="#4CAF50", fg="white", padx=15, pady=5)
btn.pack()

root.mainloop()
