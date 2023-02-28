from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Cristian First GUI Program")

icon = PhotoImage(file='img.png')
window.iconphoto(True, icon)

# window.config(background="blue")
window.config(background="#5cfcff")

window.mainloop()  # place window on computer screen, listen for events
