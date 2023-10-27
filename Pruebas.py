from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.patches as patches
from mpl_interactions import ioff, panhandler, zoom_factory
from tkinter import ttk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from tkinter import IntVar
import math

root = tk.Tk()
root.title("Prueba")
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig, master=root)

canvas.get_tk_widget().pack()
zoom_factory(ax, base_scale=1.1)
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()
toolbar.pack()
toolbar.pan()

tk.Button(text = "SI", command= lambda: draw(ax, canvas)).pack()

def draw(ax, canvas):
    img = np.asarray(Image.open("vader.jpeg"))
    ax.imshow(img)
    canvas.draw()
'''
img = np.asarray(Image.open("vader.jpeg"))
print(repr(img))

imgplot = plt.imshow(img)

plt.show()
'''
root.mainloop()