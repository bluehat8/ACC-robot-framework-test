import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    directory = filedialog.askdirectory()
    directory_label.config(text=directory)

def delete_videos():
    directory = directory_label.cget('text')
    if not directory:
        return
    for filename in os.listdir(directory):
        if filename.endswith('.mp4'):
            os.remove(os.path.join(directory, filename))
    delete_label.config(text='Videos eliminados correctamente')

root = tk.Tk()
root.title('Eliminar videos locales')

directory_button = tk.Button(root, text='Seleccionar directorio', command=select_directory)
directory_button.pack()

directory_label = tk.Label(root, text='')
directory_label.pack()

delete_button = tk.Button(root, text='Eliminar videos', command=delete_videos)
delete_button.pack()

delete_label = tk.Label(root, text='')
delete_label.pack()

root.mainloop()