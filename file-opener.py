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


root = tk.Tk()
root.title("Prototype Demo")


image_label = tk.Label(root)
image_label.pack()


open_button = tk.Button(root, text="Browse", command=open_image)
open_button.pack()


root.mainloop()