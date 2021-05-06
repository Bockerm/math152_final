from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
gcdLst = []
extLst = []

########################################################################

root = Tk()
root.title("Fermat's Little and Euler's Totient")
canvas_2 = Canvas(root, width=400, height=300)
canvas_2.grid(columnspan=3, rowspan=5) 

fInstructions = Frame(root)
instructions1 = Label(fInstructions, text="This function applies Fermat's Little theorem and Euler's Totient to compute expressions", font=iFont)
instructions2 = Label(fInstructions, text="of the form shown below where p is a prime number", font=iFont)
instructions1.pack(side='top')
instructions2.pack(side='bottom')




root.mainloop()