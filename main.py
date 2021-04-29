# This file is for creating the GUI
from functions import euclidean, extended 
from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')


########################################### EUCLIDEAN ALGORITHM
root_1 = Tk()
root_1.title("Euclidean Algorithm")
canvas_1 = Canvas(root_1, width=400, height=300)
canvas_1.grid(columnspan=2, rowspan=5)

# Instructions 

insts = Label(root_1, text='This function calculates the GCD of a and b using the euclidean algorithm', font=iFont)
insts.grid(columnspan=2, column=0, row=0)

# Inputs
f1 = Frame(root_1)
f11 = Frame(f1)
f12 = Frame(f1)
f11.pack(side='top')
f12.pack(side='bottom')
f1.grid(columnspan=1, column=0, row=1)

e1Label = Label(f11, text="a = ", font= eFont)
e1Label.pack(side='left')
e1 = Entry(f11)
e1.pack(side='right')

e2Label = Label(f12, text="b = ", font= eFont)
e2Label.pack(side='left')
e2 = Entry(f12)
e2.pack(side='right')

f2 = Frame(root_1)
f21 = Frame(f2)
f22 = Frame(f2)
f21.pack(side='top')
f22.pack(side='bottom')
f2.grid(columnspan=1, column=1, row=1)
gcdLabel = Label(f21, text='r = GCD(a,b)', font=eFont)
extLabel = Label(f22, text='r = ax + by', font=eFont)
gcdLabel.pack(side='top')
extLabel.pack(side='bottom')


# function for calculating GCD
def gcdCmd():
    # make sure input for both entries are ints
    a = e1.get()
    b = e2.get()
    row = 3 
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        a,b = max(a, b), min(a,b)
        gcdText.set('Calculating...')
        initEq = str(a) + '=' + str(b) + '(' + str(int(a/b)) + ') + ' + str(a%b) 
        initStep = Label(root_1, text=initEq, font=eFont)
        initStep.grid(columnspan=2, row=row)
        row+=1
        while (a%b) != 0:
            a,b = b, a%b
            eq = str(a) + "=" + str(b) + "(" + str(int(a/b)) + ") + " + str(a%b)
            step = Label(root_1, text=eq, font=eFont)
            step.grid(columnspan=2, row=row)
            row+=1
        gcdEq = str(b) + "= GCD(" + e1.get() + ',' + e2.get() + ')'
        gcdLabel = Label(root_1, text=gcdEq, font=eFont)
        gcdLabel.grid(columnspan=2, row=row)
    else:
        Emsg = 'Input is not an INT'
        emLabel = Label(root_1, text = Emsg, font=iFont)
        emLabel.grid(columnspan=2, row=row)
    gcdText.set('GCD using Euclidean')
    
    
def extCmd():
    # check input entries 
    # make sure input for both entries are ints
    a = e1.get()
    b = e2.get()
    row = 3 
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        a,b = max(a, b), min(a,b)
        
    return
    

# GCD button 
gcdText = StringVar()
gcdButton = Button(root_1, textvariable=gcdText, font=bFont, command=gcdCmd)
gcdText.set('GCD using Euclidean')
gcdButton.grid(columnspan=1, row=2, column=0)

# Extended 
extText = StringVar()
extButton = Button(root_1, textvariable=extText, font=bFont, command=extCmd)
extText.set('GCD and Bezout Coefficients using Extended Euclidean')
extButton.grid(columnspan=1, row=2, column=1)

root_1.mainloop()

########################################### EXTENDED EUCLIDEAN ALGORITHM
# root_2 = Tk()
# root_2.title("Extended Euclidean Algorithm")
# canvas_2 = Canvas(root_2, width=600, height=300)
# canvas_2.grid(columnspan=3, rowspan=3)

# # instructions


# ########################################### FERMAT'S LITTLE THEOREM AND EULER'S TOTIENT THEOREM
# root_3 = Tk()
# root_3.title("Fermat’s Little Theorem and Euler’s Totient Theorem")
# canvas_3 = Canvas(root_3, width=600, height=300)
# canvas_3.grid(columnspan=3, rowspan=3)

# # instructions 


# ########################################### CLOCK ARITHMETIC
# root_4 = Tk()
# root_4.title("Clock Arithmetic")
# canvas_4 = Canvas(root_4, width=600, height=300)
# canvas_4.grid(columnspan=3, rowspan=3)

# instructions 