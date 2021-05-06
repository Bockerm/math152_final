from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
widgLst = []

########################################################################

root = Tk()
root.title("Fermat's Little and Euler's Totient")
canvas = Canvas(root, width=400, height=300)
canvas.grid(columnspan=3, rowspan=5) 

fInstructions = Frame(root)
fInstructions.grid(columnspan=3, row=0)
instructions1 = Label(fInstructions, text="This function applies Fermat's Little theorem and Euler's Totient to compute expressions", font=iFont)
instructions2 = Label(fInstructions, text="of the form shown below where p is a prime number", font=iFont)
instructions1.pack(side='top')
instructions2.pack(side='bottom')


exampleEq = u"a\u207f"+" mod p"
lExampleEq = Label(root, text=exampleEq, font=('Times', '25', 'italic'))
lExampleEq.grid(columnspan=3, row=2)

leftFrame = Frame(root)
midFrame = Frame(root)
rightFrame = Frame(root)
leftFrame.grid(columnspan=1, row=3, column=0)
midFrame.grid(columnspan=1, row=3, column=1)
rightFrame.grid(columnspan=1, row=3, column=2)


aLabel = Label(leftFrame, text='a = ', font=eFont)
pLabel = Label(rightFrame, text='p = ', font=eFont)
nLabel = Label(midFrame, text='n = ', font=eFont)
aLabel.pack(side='left')
pLabel.pack(side='left')
nLabel.pack(side='left')


aEntry = Entry(leftFrame)
pEntry = Entry(rightFrame)
nEntry = Entry(midFrame)
aEntry.pack(side='right')
pEntry.pack(side='right')
nEntry.pack(side='right')

# unicode for phi \u03A6



def fermats():
    return



calcText = StringVar()
calcButton = Button(root, textvariable=calcText, font=bFont, command=fermats)
calcText.set('Compute')
calcButton.grid(columnspan=1, row=4, column=1)



root.mainloop()