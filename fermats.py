from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
widgLst = []

numSupLst = ["\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]
opsSupDict = {"+": "\u207A", "-": "\u207B", "=": "\u207C", "(": "\u207D", ")": "\u207E"}

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

# unicode for phi \u03A6 congruence \u2245 division \u2215

def clearContent(): 
    if widgLst:    
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


def superscriptEq1(a, n, p):
    global numSupLst 
    global opsSupDict 
    quotient = str(int(n/(p-1)))
    remainder = str(n - int(quotient))
    supEquation = str(p-1) + "(" + quotient + ")" + "+" + remainder
    supUniStr = str(a)
    for char in supEquation:
        if char.isdigit():  
            supUniStr = supUniStr + numSupLst[int(char)]
        else:
            supUniStr = supUniStr + opsSupDict.get(char)
    return supUniStr

def helper(s1, s2):
        for char in s2:
            s1 = s1 + numSupLst[int(char)]
        return s1


# unicode asterisk \u2217 cross product \u2A2F
def superscriptEq2(a, n, p):
    global numSupLst 

    quotient = str(int(n/(p-1)))
    remainder = str(n - int(quotient))
    a = str(a) 
    exp1 = helper(a, str(p-1))
    exp2 = helper(")", str(quotient)) 
    exp3 = helper(a, remainder)
    eq = "(" + exp1 + exp2 + " " + u"\u2A2F" + " " + exp3 
    return eq



def fermats():
    global widgLst
    clearContent()
    calcText.set("Calculating...")
    row = 5
    a = aEntry.get()
    p = int(pEntry.get())
    n = nEntry.get()
    if not isprime(p):
        errorMSG = 'p is not a prime number'
        errorLabel = Label(root, text=errorMSG, font=iFont)
        errorLabel.grid(columnspan=3, row=row)
        widgLst.append(errorLabel)
        row+=1
    elif not a.isdigit() or not n.isdigit():
        errorMSG = 'a and or n is not an int'
        errorLabel = Label(root, text=errorMSG, font=iFont)
        errorLabel.grid(columnspan=3, row=row)
        widgLst.append(errorLabel)
        row+=1
    else:
        a = int(a)
        n = int(n)
        step1Text = "Apply Euler's Totient Theorem to n"
        step1Label = Label(root, text=step1Text, font=eFont)
        step1Label.grid(columnspan=3, row=row, column=0)
        widgLst.append(step1Label)
        row+=1

        totientEq = str(p) + " - 1 = " + str(p-1)
        totientLabel = Label(root, text=totientEq, font=eFont)
        totientLabel.grid(columnspan=1, row=row, column=1)
        widgLst.append(totientLabel)
        row+=1

        step2Text = "Apply Fermat's Little Theorem"
        step2Label = Label(root, text=step2Text, font=eFont)
        step2Label.grid(columnspan=3, row=row, column=0)
        widgLst.append(step2Label)
        row+=1

        fermats1 = superscriptEq1(a, n, p)
        fermats1L = Label(root, text=fermats1, font=eFont)
        fermats1L.grid(columnspan=1, row=row, column=1)
        widgLst.append(fermats1L)
        row+=1
        
        fermats2 = superscriptEq2(a, n, p)
        fermats2L = Label(root, text=fermats2, font=eFont)
        fermats2L.grid(columnspan=1, row=row, column=1)
        widgLst.append(fermats2L)
        row+=1

        fermats3 = helper(str(1), str(int(n/(p-1)))) + " " + u"\u2A2F" + " " + str(a**(n%(p-1))) + " ( mod " + str(p) + ")" 
        fermats3L = Label(root, text=fermats3, font=eFont)
        fermats3L.grid(columnspan=1, row=row, column=1)
        widgLst.append(fermats3L)
        

        applyF = "Fermat's Little Theorem"
        applyFL = Label(root, text=applyF, font=iFont)
        applyFL.grid(columnspan=1, row=row, column=2)
        widgLst.append(applyFL)
        row+=1

        penult = str((a**(n%(p-1)))%p) + " ( mod " + str(p) + ")" 
        penultL = Label(root, text=penult, font=eFont)
        penultL.grid(columnspan=1, row=row, column=1)
        widgLst.append(penultL)
        row+=1

        finalEq = helper(str(a), str(n)) + " ( mod " + str(p) + ") = " + str((a**(n%(p-1)))%p) 
        finalEqL = Label(root, text=finalEq, font=eFont)
        finalEqL.grid(columnspan=1, row=row, column=1)
        widgLst.append(finalEqL)
        row+=1
    
    buffer = Label(root)
    buffer.grid(columnspan=3, row=row)
    widgLst.append(buffer)
    calcText.set('Compute')

    






calcText = StringVar()
calcButton = Button(root, textvariable=calcText, font=bFont, command=fermats)
calcText.set('Compute')
calcButton.grid(columnspan=1, row=4, column=1)



root.mainloop()