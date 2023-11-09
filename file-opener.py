import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    # Get the file path of the image
    filepath = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])

    # Check if the user selected an image
    if filepath:
        # Load the image using Pillow
        image = Image.open(filepath)

        # Resize the image to fit the label
        resized_image = image.resize((300, 300), Image.ANTIALIAS)

        # Convert the image to a PhotoImage
        photoimage = ImageTk.PhotoImage(resized_image)

        # Display the image in the label
        image_label.configure(image=photoimage)
        image_label.image = photoimage

# Create the main window
root = tk.Tk()
root.title("Prototype Demo")

# Create a label for the image
image_label = tk.Label(root)
image_label.pack()

# Create a button to open the file dialog
open_button = tk.Button(root, text="Browse", command=open_image)
open_button.pack()

# Run the main loop
root.mainloop()