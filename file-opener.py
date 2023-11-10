import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global image_object
    filepath = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if filepath:
        image = Image.open(filepath)
        resized_image = image.resize((400, 200), Image.ANTIALIAS)
        photoimage = ImageTk.PhotoImage(resized_image)

        if image_object is not None:
            image_object.destroy()

        image_object = photoimage
        image_label.configure(image=photoimage)

def update_table():
    predicted_roll_no = "NULL"  
    table_value.set(predicted_roll_no)

root = tk.Tk()
root.title("Prototype Demo")

header_label = tk.Label(root, text="Prototype Demonstration App", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

image_label = tk.Label(root, image=None)
image_label.pack()

image_object = None

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'))

style.configure(
    'Browse.TButton',
    foreground='white',
    background='#007bff',
)

open_button = ttk.Button(root, text="Browse", command=open_image, style='TButton')
open_button.pack(pady=10)

table_frame = ttk.Frame(root)
table_frame.pack(pady=10)

left_cell_label = ttk.Label(table_frame, text="Predicted Roll No:", font=("Helvetica", 10, "bold"))
left_cell_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

table_value = tk.StringVar()
right_cell_label = ttk.Label(table_frame, textvariable=table_value, font=("Helvetica", 10, "bold"))
right_cell_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)


update_table()

root.mainloop()
