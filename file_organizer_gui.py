from tkinter import *
from tkinter import filedialog
import os, shutil

def organize_files():
    folder = filedialog.askdirectory()
    if not folder:
        return

    file_types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            moved = False
            for folder_name, extensions in file_types.items():
                for ext in extensions:
                    if file.lower().endswith(ext):
                        os.makedirs(os.path.join(folder, folder_name), exist_ok=True)
                        shutil.move(file_path, os.path.join(folder, folder_name, file))
                        moved = True
                        break
                if moved:
                    break
            
            if not moved:
                os.makedirs(os.path.join(folder, "Others"), exist_ok=True)
                shutil.move(file_path, os.path.join(folder, "Others", file))

    status_label.config(text="Files Organized Successfully!")

root = Tk()
root.title("File Organizer")

Button(root, text="Select Folder & Organize", command=organize_files).pack(pady=10)
status_label = Label(root, text="")
status_label.pack()

root.mainloop()