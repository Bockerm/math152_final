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

def clearContent(): 
    l = len(widgLst)
    for i in range(l):
        widgLst[l-(i+1)].destroy()
        del widgLst[l - (i+1)]
  

def isprime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False



def fermats():
    global widgLst
    row = 5
    a = int(aEntry.get())
    p = int(pEntry.get())
    n = int(nEntry.get())
    if not isprime(p):
        errorMSG = 'p is not a prime number'
        errorLabel = Label(root, text=errorMSG, font=iFont)
        errorLabel.grid(columnspan=3, row=row)
        widgLst.append(errorLabel)
    else:
        step1Text = "Apply Euler's Totient Theorem to n"
        step1Label = Label(root, text=step1Text, font=eFont)
        step1Label.grid(columnspan=3, row=row)
        widgLst.append(step1Label)
        row+=1


        totientEq = str(p) + " - 1 = " + str(p-1)
        totientLabel = Label(root, text=totientEq, font=eFont)
        totientLabel.grid(columnspan=3, row=row)
        widgLst.append(totientLabel)
        row+=1

        step2Text = "Apply Fermat's Little Theorem"
        step2Label = Label(root, text=step2Text, font=eFont)
        step2Label.grid(columnspan=3, row=row)
        widgLst.append(step2Label)
        row+=1

        # fermats1 = 
    



calcText = StringVar()
calcButton = Button(root, textvariable=calcText, font=bFont, command=fermats)
calcText.set('Compute')
calcButton.grid(columnspan=1, row=4, column=1)



root.mainloop()