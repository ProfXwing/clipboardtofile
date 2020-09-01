from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename


def end_script():
    input("Press enter to end script.\n")


saved = False

while not saved:
    try:
        im = ImageGrab.grabclipboard()
        Tk().withdraw()
        directory = asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        im.save(f'{directory}', 'PNG')
        saved = True
    except AttributeError:
        print("Cannot save anything but image. Please use WINDOWS + SHIFT + S")
        break
    except FileNotFoundError:
        print("Please choose a directory next time.")
        break
    except Exception as e:
        print(f"Something went wrong. I don't know what. Here's the error: {e}")
        input("Try to fix it, I guess.")
        break
    if saved:
        print(f"Image saved to {directory}")
        break
end_script()
