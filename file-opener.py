import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    filepath = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if filepath:
        image = Image.open(filepath)
        resized_image = image.resize((300, 150), Image.ANTIALIAS)
        photoimage = ImageTk.PhotoImage(resized_image)

        image_label.configure(image=photoimage)
        image_label.image = photoimage

        image_label_below.configure(image=photoimage)
        image_label_below.image = photoimage

root = tk.Tk()
root.title("Image Info App")

# Create a header label
header_label = tk.Label(root, text="Image Information App", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

image_label_below = tk.Label(root)
image_label_below.pack()

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'))

style.configure(
    'Browse.TButton',
    foreground='white', 
    background='#007bff', 
)

open_button = ttk.Button(root, text="Browse", command=open_image, style='TButton')
open_button.pack(pady=10)

root.mainloop()
