import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    filepath = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if filepath:
        image = Image.open(filepath)
        resized_image = image.resize((300, 300), Image.ANTIALIAS)
        photoimage = ImageTk.PhotoImage(resized_image)

        image_label.configure(image=photoimage)
        image_label.image = photoimage

        image_label_below.configure(image=photoimage)
        image_label_below.image = photoimage

        name_entry.config(state=tk.NORMAL)
        location_entry.config(state=tk.NORMAL)
        description_entry.config(state=tk.NORMAL)

def save_info():
    name = name_var.get()
    location = location_var.get()
    description = description_var.get()

    print(f"Name: {name}, Location: {location}, Description: {description}")

    name_var.set('')
    location_var.set('')
    description_var.set('')

root = tk.Tk()
root.title("Prototype Demo")

image_label = tk.Label(root)
image_label.pack()

image_label_below = tk.Label(root)
image_label_below.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var, state=tk.DISABLED)
name_entry.pack()

location_label = tk.Label(root, text="Location:")
location_label.pack()
location_var = tk.StringVar()
location_entry = tk.Entry(root, textvariable=location_var, state=tk.DISABLED)
location_entry.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()
description_var = tk.StringVar()
description_entry = tk.Entry(root, textvariable=description_var, state=tk.DISABLED)
description_entry.pack()

open_button = tk.Button(root, text="Browse", command=open_image)
open_button.pack()

save_button = tk.Button(root, text="Save Information", command=save_info, state=tk.DISABLED)
save_button.pack()

def enable_save_button(event):
    if name_var.get() and location_var.get() and description_var.get():
        save_button.config(state=tk.NORMAL)
    else:
        save_button.config(state=tk.DISABLED)

name_var.trace("w", enable_save_button)
location_var.trace("w", enable_save_button)
description_var.trace("w", enable_save_button)

root.mainloop()
