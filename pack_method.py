from tkinter import *
# creating Tk window
pane = Tk()

b1 = Button(pane, text  = "Click me !")
b1.pack(fill=Y, expand = True,pady=20)

# Button 2
b2 = Button(pane, text = "Click me too")
b2.pack(fill = X, expand = True,pady=300,padx=100)

# Execute Tkinter
pane.mainloop()

