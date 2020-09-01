from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
saved = False
while not saved:
    im = ImageGrab.grabclipboard()
    Tk().withdraw()
    directory = asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    im.save(f'{directory}', 'PNG')
    saved = True
