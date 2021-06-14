#!/usr/bin/env python3

import tkinter
import sys

# Fenster aufbauen #####################################################
root = tkinter.Tk()
root.overrideredirect(1) # Fenster ohne aussen rum :-)
#root.attributes('-topmost', 1) # Fenster immer im Vordergrund
#root.attributes('-zoomed', True) # Fenster zoomed
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry('%dx%d' % (w,h))
root.wait_visibility(root)
root.attributes('-alpha', 0.7) # Fenster transparent

# Text einlesen ########################################################
params = sys.argv
if (len(params) > 2):
  txt = params[1] + " - " + params[2]
else:
  txt = "ENDE"

# Text und Button ausgeben #############################################
FONT = "{Verdana} 50 bold"
text = tkinter.Text(root,relief=tkinter.FLAT, font=FONT, height=10, bg='black', fg='red')
text.pack(expand=tkinter.YES, fill=tkinter.BOTH)
text.insert(tkinter.END, txt)

button = tkinter.Button(root, text='Quit', bd=1, command=quit)
button.pack(side=tkinter.BOTTOM, fill=tkinter.X)

root.mainloop()
