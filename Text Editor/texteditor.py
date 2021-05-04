#Imports
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#Screen
root=Tk("Text Editor")
text=Text(root)
text.grid()

#Save as
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
#Save as Button
button1=Button(root, text="Save as", command=saveas)
button1.grid() 

#Run
root.mainloop() 