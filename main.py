# This file is for creating the GUI
from functions import test 
from tkinter import *

# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')


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
f2 = Frame(root_1)
f1.grid(columnspan=1, column=0, row=1)
f2.grid(columnspan=1, column=1, row=1)

aLabel = Label(f1, text="a = ", font= eFont)
aLabel.pack(side='left')
a = Entry(f1)
a.insert(0, "Enter a positive int")
a.pack(side='right')

bLabel = Label(f2, text="b = ", font= eFont)
bLabel.pack(side='left')
b = Entry(f2)
b.insert(0, 'Enter a positive int')
b.pack(side='right')

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