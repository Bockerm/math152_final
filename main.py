# This file is for creating the GUI

from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
gcdLst = []
extLst = []

########################################### EUCLIDEAN and EXTENDED EUCLIDEAN 
root = Tk()
root.title("Euclidean Algorithm")
canvas_1 = Canvas(root, width=400, height=300)
canvas_1.grid(columnspan=3, rowspan=5)

# Instructions 
fTitle = Frame(root)
insts = Label(fTitle, text='This function calculates the GCD and/or Bezout Coefficients of a and b using the euclidean', font=iFont)
insts_2 = Label(fTitle, text='and extended euclidean algorithms', font=iFont)
buffer = Label(root)
buffer.grid(columnspan=3, row=1)
insts.pack(side='top')
insts_2.pack(side='bottom')
fTitle.grid(columnspan=3, row=0)

# Inputs
f1 = Frame(root)
f11 = Frame(f1)
f12 = Frame(f1)
f11.pack(side='top')
f12.pack(side='bottom')
f1.grid(columnspan=1, column=0, row=2)

e1Label = Label(f11, text="a = ", font= eFont)
e1Label.pack(side='left')
e1 = Entry(f11)
e1.pack(side='right')

e2Label = Label(f12, text="b = ", font= eFont)
e2Label.pack(side='left')
e2 = Entry(f12)
e2.pack(side='right')

f2 = Frame(root)
f21 = Frame(f2)
f22 = Frame(f2)
f21.pack(side='top')
f22.pack(side='bottom')
f2.grid(columnspan=2, column=1, row=2)
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
    emLabel = Label(root, text = s, font=iFont)
    emLabel.grid(columnspan=3, row=row)


# function for calculating GCD
def gcdCmd():
    global gcdLst 
    clearContent()
    # make sure input for both entries are ints
    a = e1.get()
    b = e2.get()
    row = 4
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        a,b = max(a, b), min(a,b)
        gcdText.set('Calculating...')
        initEq = str(a) + '=' + str(b) + '(' + str(int(a/b)) + ') + ' + str(a%b) 
        initStep = Label(root, text=initEq, font=eFont)
        initStep.grid(columnspan=3, row=row)
        gcdLst.append(initStep)
        row+=1
        while (a%b) != 0:
            a,b = b, a%b
            eq = str(a) + "=" + str(b) + "(" + str(int(a/b)) + ") + " + str(a%b)
            step = Label(root, text=eq, font=eFont)
            step.grid(columnspan=3, row=row)
            gcdLst.append(step)
            row+=1
        gcdEq = str(b) + "= GCD(" + e1.get() + ',' + e2.get() + ')'
        gcdLabel = Label(root, text=gcdEq, font=eFont)
        gcdLabel.grid(columnspan=3, row=row)
        gcdLst.append(gcdLabel)
        row+=1

        buffer = Label(root)
        buffer.grid(columnspan=3, row=row)
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
    row = 4
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
        rExampleL = Label(root, text=rExampleEq, font=eFont)
        rExampleL.grid(columnspan=1, row=row, column=0)
        extLst.append(rExampleL)

        sExampleEq = u"s\u2096\u208a\u2081" + " = " + u"s\u2096\u208b\u2081" + " - " + u"s\u2096" + u"q\u2096"
        sExampleL = Label(root, text=sExampleEq, font=eFont)
        sExampleL.grid(columnspan=1, row=row, column=1)
        extLst.append(sExampleL)

        tExampleEq = u"t\u2096\u208a\u2081" + " = " + u"t\u2096\u208b\u2081" + " - " + u"t\u2096" + u"q\u2096   "
        tExampleL = Label(root, text=tExampleEq, font=eFont)
        tExampleL.grid(columnspan=1, row=row, column=2)
        extLst.append(tExampleL)
        row+=1

        rInitEq = str(a%b) + ' = '  + str(a) + " - " + str(b) + '(' + str(int(a/b)) + ')' 
        rInitStep = Label(root, text=rInitEq, font=eFont)
        rInitStep.grid(columnspan=1, row=row, column=0)
        extLst.append(rInitStep)
        
        s_new = s_i-s_j*(int(a/b))
        sInitEq = str(s_new) + ' = '  + str(s_i)  + " - "  + str(s_j) + '(' + str(int(a/b)) + ')' 
        sInitStep = Label(root, text=sInitEq, font=eFont)
        sInitStep.grid(columnspan=1, row=row, column=1)
        extLst.append(sInitStep)

        t_new = t_i-t_j*(int(a/b))
        tInitEq = str(t_new) + ' = '  + str(t_i) + " - " + str(t_j) + '(' + str(int(a/b)) + ')' 
        tInitStep = Label(root, text=tInitEq, font=eFont)
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
            rStep = Label(root, text=rEq, font=eFont)
            rStep.grid(columnspan=1, row=row, column=0)
            extLst.append(rStep)
            
            sgn = " - "
            if s_j < 0:
                sgn = " + "
            sEq = str(s_new) + ' = '  + str(s_i) + sgn + str(abs(s_j)) + '(' + str(int(a/b)) + ')' 
            sStep = Label(root, text=sEq, font=eFont)
            sStep.grid(columnspan=1, row=row, column=1)
            extLst.append(sStep)

            sgn = " - "
            if t_j < 0:
                sgn = " + "
            tEq = str(t_new) + ' = '  + str(t_i) + sgn + str(abs(t_j)) + '(' + str(int(a/b)) + ')' 
            tStep = Label(root, text=tEq, font=eFont)
            tStep.grid(columnspan=1, row=row, column=2)
            extLst.append(tStep)
            row+=1
        
        rFinalEq = u"r\u2096" " = " + str(b)
        rFinalL = Label(root, text=rFinalEq, font=eFont)
        rFinalL.grid(columnspan=1, row=row, column=0)
        extLst.append(rFinalL)

        sFinalEq = u"s\u2096" + " = " + str(s_j) 
        sFinalL = Label(root, text=sFinalEq, font=eFont)
        sFinalL.grid(columnspan=1, row=row, column=1)
        extLst.append(sFinalL)

        tFinalEq = u"t\u2096" + " = " + str(t_j)
        tFinalL = Label(root, text=tFinalEq, font=eFont)
        tFinalL.grid(columnspan=1, row=row, column=2)
        extLst.append(tFinalL)
        row+=1

        refLabel = Label(root, text=u"r\u2096"+"= a"+u"s\u2096"+"+ b"+u"t\u2096", font=eFont)
        refLabel.grid(columnspan=3, row=row)
        extLst.append(refLabel)
        row+=1

        finalEq = str(b) + " = " + str(aF) + "(" + str(s_j) + ") + " + str(bF) + "(" + str(t_j) + ")"
        finalL = Label(root, text=finalEq, font=eFont)
        finalL.grid(columnspan=3, row=row)
        extLst.append(finalL)
        row+=1

        buffer = Label(root)
        buffer.grid(columnspan=3, row=row)
    else:
        Emsg = 'Input is not an INT'
        errormessage(Emsg, row)
    extText.set('GCD and Bezout Coefficients using Extended Euclidean')
    

# GCD button 
gcdText = StringVar()
gcdButton = Button(root, textvariable=gcdText, font=bFont, command=gcdCmd)
gcdText.set('GCD using Euclidean')
gcdButton.grid(columnspan=1, row=3, column=0)

# Extended 
extText = StringVar()
extButton = Button(root, textvariable=extText, font=bFont, command=extCmd)
extText.set('GCD and Bezout Coefficients using Extended Euclidean')
extButton.grid(columnspan=2, row=3, column=1)

root.mainloop()





