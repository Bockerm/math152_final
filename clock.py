from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
gcdLst = []
extLst = []


########################################################################

root = Tk()
root.title("Clock Arithmetic")
canvas = Canvas(root, width=400, height=300)
canvas.grid(columnspan=3, rowspan=5) 

fInstructions = Frame(root)
instructions1 = Label(fInstructions, text="This function applies modular arithmetic to find day of week/time of day given a certain", font=iFont)
instructions2 = Label(fInstructions, text="number of hours, days, months and/or years from a starting date", font=iFont)
instructions1.pack(side='top')
instructions2.pack(side='bottom')

buffer = Label(root)
buffer.grid(columnspan=3, row=1)








root.mainloop()