from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_interactions import zoom_factory
from tkinter import IntVar


var = "vader"
root = tk.Tk()
root.title("Prueba")
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Define a function to update the image position and size
def update_image_position_and_size(x, y, width, height):
    img = np.asarray(Image.open(var + ".jpeg"))
    ax.imshow(img, extent=[x, x + width, y, y + height])
    canvas.draw()

# Initial position and size of the image
x = 0  # X-coordinate of the top-left corner
y = 0  # Y-coordinate of the top-left corner
width = 300  # Width of the image
height = 200  # Height of the image

update_image_position_and_size(x, y, width, height)

# Create tkinter Entry widgets to input new position and size
x_entry = tk.Entry(root, width=5)
x_entry.insert(0, str(x))
x_entry.pack()
y_entry = tk.Entry(root, width=5)
y_entry.insert(0, str(y))
y_entry.pack()
width_entry = tk.Entry(root, width=5)
width_entry.insert(0, str(width))
width_entry.pack()
height_entry = tk.Entry(root, width=5)
height_entry.insert(0, str(height))
height_entry.pack()

# Create a button to update the image position and size
update_button = tk.Button(
    text="Update Image",
    command=lambda: update_image_position_and_size(
        float(x_entry.get()),
        float(y_entry.get()),
        float(width_entry.get()),
        float(height_entry.get())
    ),
)
update_button.pack()

root.mainloop()
