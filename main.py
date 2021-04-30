# This file is for creating the GUI
from functions import euclidean, extended 
from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
gcdLst = []
extLst = []

########################################### EUCLIDEAN and EXTENDED EUCLIDEAN 
root_1 = Tk()
root_1.title("Euclidean Algorithm")
canvas_1 = Canvas(root_1, width=400, height=300)
canvas_1.grid(columnspan=3, rowspan=5)

# Instructions 
fTitle = Frame(root_1)
insts = Label(fTitle, text='This function calculates the GCD and/or Bezout Coefficients of a and b using the euclidean', font=iFont)
insts_2 = Label(fTitle, text='and extended euclidean algorithms', font=iFont)
insts.pack(side='top')
insts_2.pack(side='bottom')
fTitle.grid(columnspan=3, row=0)

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
f2.grid(columnspan=2, column=1, row=1)
gcdLabel = Label(f21, text=u"r\u2096"+" = GCD(a,b)", font=eFont)
extLabel = Label(f22, text=u"r\u2096"+"= a"+u"s\u2096"+"+ b"+u"t\u2096", font=eFont)
gcdLabel.pack(side='top')
extLabel.pack(side='bottom')

def clearContent():
    def helper(lst):
        l = len(lst)
        for i in range(l):
            lst[l-(i+1)].destroy()
            del lst[l - (i+1)]
    if gcdLst:
        helper(gcdLst)
    elif extLst:
        helper(extLst)
    else:
        try:
            emLabel.destroy()
        except:
            pass


def errormessage(s, row):
    global emLabel
    emLabel = Label(root_1, text = s, font=iFont)
    emLabel.grid(columnspan=3, row=row)


# function for calculating GCD
def gcdCmd():
    global gcdLst 
    clearContent()
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
        initStep.grid(columnspan=3, row=row)
        gcdLst.append(initStep)
        row+=1
        while (a%b) != 0:
            a,b = b, a%b
            eq = str(a) + "=" + str(b) + "(" + str(int(a/b)) + ") + " + str(a%b)
            step = Label(root_1, text=eq, font=eFont)
            step.grid(columnspan=3, row=row)
            gcdLst.append(step)
            row+=1
        gcdEq = str(b) + "= GCD(" + e1.get() + ',' + e2.get() + ')'
        gcdLabel = Label(root_1, text=gcdEq, font=eFont)
        gcdLabel.grid(columnspan=3, row=row)
        gcdLst.append(gcdLabel)
    else:
        Emsg = 'Input is not an INT'
        errormessage(Emsg, row)
    gcdText.set('GCD using Euclidean')
    
    
def extCmd():
    global extLst 
    clearContent()
    
    # make sure input for both entries are ints
    a = e1.get()
    b = e2.get()
    row = 3 
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        a,b = max(a, b), min(a,b)
        aF = a 
        bF = b
        s_i=1
        s_j=0
        t_i=0
        t_j=1
        extText.set('Calculating...')

        rExampleEq = u"r\u2096\u208a\u2081" + " = " + u"r\u2096\u208b\u2081" + " - " + u"r\u2096" + u"q\u2096"
        rExampleL = Label(root_1, text=rExampleEq, font=eFont)
        rExampleL.grid(columnspan=1, row=row, column=0)
        extLst.append(rExampleL)

        sExampleEq = u"s\u2096\u208a\u2081" + " = " + u"s\u2096\u208b\u2081" + " - " + u"s\u2096" + u"q\u2096"
        sExampleL = Label(root_1, text=sExampleEq, font=eFont)
        sExampleL.grid(columnspan=1, row=row, column=1)
        extLst.append(sExampleL)

        tExampleEq = u"t\u2096\u208a\u2081" + " = " + u"t\u2096\u208b\u2081" + " - " + u"t\u2096" + u"q\u2096   "
        tExampleL = Label(root_1, text=tExampleEq, font=eFont)
        tExampleL.grid(columnspan=1, row=row, column=2)
        extLst.append(tExampleL)
        row+=1

        rInitEq = str(a%b) + ' = '  + str(a) + " - " + str(b) + '(' + str(int(a/b)) + ')' 
        rInitStep = Label(root_1, text=rInitEq, font=eFont)
        rInitStep.grid(columnspan=1, row=row, column=0)
        extLst.append(rInitStep)
        
        s_new = s_i-s_j*(int(a/b))
        sInitEq = str(s_new) + ' = '  + str(s_i)  + " - "  + str(s_j) + '(' + str(int(a/b)) + ')' 
        sInitStep = Label(root_1, text=sInitEq, font=eFont)
        sInitStep.grid(columnspan=1, row=row, column=1)
        extLst.append(sInitStep)

        t_new = t_i-t_j*(int(a/b))
        tInitEq = str(t_new) + ' = '  + str(t_i) + " - " + str(t_j) + '(' + str(int(a/b)) + ')' 
        tInitStep = Label(root_1, text=tInitEq, font=eFont)
        tInitStep.grid(columnspan=1, row=row, column=2)
        extLst.append(tInitStep)
        row+=1
        
        while (a%b) != 0:
            a, b = b, a%b
            t_j, t_i = t_new, t_j
            s_j, s_i = s_new, s_j
            s_new = s_i-s_j*(int(a/b))
            t_new = t_i-t_j*(int(a/b))

            rEq = str(a%b) + ' = '  + str(a) + " - " + str(b) + '(' + str(int(a/b)) + ')' 
            rStep = Label(root_1, text=rEq, font=eFont)
            rStep.grid(columnspan=1, row=row, column=0)
            extLst.append(rStep)
            
            sgn = " - "
            if s_j < 0:
                sgn = " + "
            sEq = str(s_new) + ' = '  + str(s_i) + sgn + str(abs(s_j)) + '(' + str(int(a/b)) + ')' 
            sStep = Label(root_1, text=sEq, font=eFont)
            sStep.grid(columnspan=1, row=row, column=1)
            extLst.append(sStep)

            sgn = " - "
            if t_j < 0:
                sgn = " + "
            tEq = str(t_new) + ' = '  + str(t_i) + sgn + str(abs(t_j)) + '(' + str(int(a/b)) + ')' 
            tStep = Label(root_1, text=tEq, font=eFont)
            tStep.grid(columnspan=1, row=row, column=2)
            extLst.append(tStep)
            row+=1
        
        rFinalEq = u"r\u2096" " = " + str(b)
        rFinalL = Label(root_1, text=rFinalEq, font=eFont)
        rFinalL.grid(columnspan=1, row=row, column=0)
        extLst.append(rFinalL)

        sFinalEq = u"s\u2096" + " = " + str(s_j) 
        sFinalL = Label(root_1, text=sFinalEq, font=eFont)
        sFinalL.grid(columnspan=1, row=row, column=1)
        extLst.append(sFinalL)

        tFinalEq = u"t\u2096" + " = " + str(t_j)
        tFinalL = Label(root_1, text=tFinalEq, font=eFont)
        tFinalL.grid(columnspan=1, row=row, column=2)
        extLst.append(tFinalL)
        row+=1

        refLabel = Label(root_1, text=u"r\u2096"+"= a"+u"s\u2096"+"+ b"+u"t\u2096", font=eFont)
        refLabel.grid(columnspan=3, row=row)
        extLst.append(refLabel)
        row+=1

        finalEq = str(b) + " = " + str(aF) + "(" + str(s_j) + ") + " + str(bF) + "(" + str(t_j) + ")"
        finalL = Label(root_1, text=finalEq, font=eFont)
        finalL.grid(columnspan=3, row=row)
        extLst.append(finalL)
        row+=1

        buffer = Label(root_1)
        buffer.grid(columnspan=3, row=row)
    else:
        Emsg = 'Input is not an INT'
        errormessage(Emsg, row)
    extText.set('GCD and Bezout Coefficients using Extended Euclidean')
    

# GCD button 
gcdText = StringVar()
gcdButton = Button(root_1, textvariable=gcdText, font=bFont, command=gcdCmd)
gcdText.set('GCD using Euclidean')
gcdButton.grid(columnspan=1, row=2, column=0)

# Extended 
extText = StringVar()
extButton = Button(root_1, textvariable=extText, font=bFont, command=extCmd)
extText.set('GCD and Bezout Coefficients using Extended Euclidean')
extButton.grid(columnspan=2, row=2, column=1)

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