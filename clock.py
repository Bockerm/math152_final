from tkinter import *
from datetime import date
from datetime import datetime



# Global variables
iFont = ('Raleway', '18', 'bold')
eFont = ('Times', '20', 'italic')
bFont = ('Raleway', '15')
widgLst = []
day_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}



########################################################################

root = Tk()
root.title("Clock Arithmetic")
canvas = Canvas(root, width=400, height=300)
canvas.grid(columnspan=4, rowspan=7) 

fInstructions = Frame(root)
instructions1 = Label(fInstructions, text="This function applies modular arithmetic to find date/day of week/time of day given a certain", font=iFont)
instructions2 = Label(fInstructions, text="number of hours, days, months and/or years from a starting date", font=iFont)
instructions1.pack(side='top')
instructions2.pack(side='bottom')
fInstructions.grid(columnspan=4, row=0)

buffer = Label(root)
buffer.grid(columnspan=4, row=1)

# Start Date Inputs
stDateL = Label(root, text='Start Date: ', font=iFont)
stDateL.grid(columnspan=1, row=2, column=0)

syrFrame = Frame(root)
smonthFrame = Frame(root)
sdayFrame = Frame(root)
syrFrame.grid(columnspan=1, row=2, column=1)
smonthFrame.grid(columnspan=1, row=2, column=2)
sdayFrame.grid(columnspan=1, row=2, column=3)

syLabel = Label(syrFrame, text='Year: ', font=eFont)
smLabel = Label(smonthFrame, text='Month: ', font=eFont)
sdLabel = Label(sdayFrame, text='Day: ', font=eFont)
syLabel.pack(side='left')
smLabel.pack(side='left')
sdLabel.pack(side='left')

syEntry = Entry(syrFrame)
smEntry = Entry(smonthFrame)
sdEntry = Entry(sdayFrame)
syEntry.pack(side='right')
smEntry.pack(side='right')
sdEntry.pack(side='right')

buffer2 = Label(root)
buffer2.grid(columnspan=4, row=3)

# Inputs
yrFrame = Frame(root)
monthFrame = Frame(root)
dayFrame = Frame(root)
hrFrame = Frame(root)
yrFrame.grid(columnspan=1, row=4, column=0)
monthFrame.grid(columnspan=1, row=4, column=1)
dayFrame.grid(columnspan=1, row=4, column=2)
hrFrame.grid(columnspan=1, row=4, column=3)

yLabel = Label(yrFrame, text='# Years: ', font=eFont)
mLabel = Label(monthFrame, text='# Months: ', font=eFont)
dLabel = Label(dayFrame, text='# Days: ', font=eFont)
hLabel = Label(hrFrame, text='# Hours: ', font=eFont)
yLabel.pack(side='left')
mLabel.pack(side='left')
dLabel.pack(side='left')
hLabel.pack(side='left')

yEntry = Entry(yrFrame)
mEntry = Entry(monthFrame)
dEntry = Entry(dayFrame)
hEntry = Entry(hrFrame)
yEntry.pack(side='right')
mEntry.pack(side='right')
dEntry.pack(side='right')
hEntry.pack(side='right')

def clearContent(): 
    if widgLst:    
        l = len(widgLst)
        for i in range(l):
            widgLst[l-(i+1)].destroy()
            del widgLst[l - (i+1)]


def clock():
    row = 6
    global widgLst
    global day_of_week
    clearContent()
    calcText.set("Calculating...")
    stY = int(syEntry.get())
    stM = int(smEntry.get())
    stD = int(sdEntry.get())
    yrs = yEntry.get()
    months = mEntry.get()
    days = dEntry.get()
    hrs = hEntry.get()
    
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def is_valid_date(year, month, day):
        if year%4==0 and (year%100 != 0 or year%400==0):
            day_count_for_month[2] = 29
        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

    if not is_valid_date(stY, stM, stD):
        errorMSG = 'Invalid Starting date'
        errorLabel = Label(root, text=errorMSG, font=iFont)
        errorLabel.grid(columnspan=4, row=row)
        widgLst.append(errorLabel)
        row+=1
    elif not yrs.isdigit() or not months.isdigit() or not days.isdigit() or not hrs.isdigit():
        errorMSG = 'All inputs must be integers or 0'
        errorLabel = Label(root, text=errorMSG, font=iFont)
        errorLabel.grid(columnspan=4, row=row)
        widgLst.append(errorLabel)
        row+=1
    else:
        yrs = int(yrs)
        months = int(months)
        days = int(days)
        hrs = int(hrs)
        if months >= 12:
            yrs = yrs + int(months/12)
            months = months%12
        if hrs >= 24:
            days = days + int(hrs/24)
            hrs = hrs%24
        if yrs > 0 or months > 0:
            d0 = date(stY, stM, stD)
            d1 = date(stY + yrs + int((stM+months)/12), (stM+months)%12, 1)
            delta = d1 - d0
            days = days + delta.days
            days = days + stD - 1
        initDay = datetime(stY, stM, stD).weekday()
        days = days - 7 + int(initDay)
        weekday = days%7
        weekday = day_of_week.get(weekday)

        dowLabel = Label(root, text='Day of Week: ' + weekday, font=eFont)
        dowLabel.grid(columnspan=1, row=row, column=1)
        widgLst.append(dowLabel)

        todLabel = Label(root, text="Hour of Day: " + str(hrs)+":00", font=eFont)
        todLabel.grid(columnspan=1, row=row, column=2)
        widgLst.append(todLabel)
        row+=1

        buffer = Label(root)
        buffer.grid(columnspan=4, row=row)
        widgLst.append(buffer)
        calcText.set('Compute')


calcText = StringVar()
calcButton = Button(root, textvariable=calcText, font=bFont, command=clock)
calcText.set('Compute')
calcButton.grid(columnspan=4, row=5)


root.mainloop()