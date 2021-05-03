# Use this file to write the various functions
# Try to write them from scratch

def euclidean(a, b):
    a, b = max(a,b), min(a,b)
    r = a%b
    if  r == 0:
        return print(b)
    else:
        euclidean(b, r)


def extended(a, b, s_i=1, s_j=0, t_i=0, t_j=1):
    a, b = max(a,b), min(a,b)
    r = a%b
    q = int(a/b)
    t_new = t_i - q*t_j
    s_new = s_i - q*s_j
    if  r == 0:
        return print(s_j, t_j)
    else:
        extended(b, r, s_j, s_new, t_j, t_new)

def totient()
    return

# assumming you start off the week on a Sunday
def clockarithmetic (hours):
    timeofday = hours%24
    daysover = (hours-timeofday)/7
    if daysover == 1:
        Day = "Monday"
    if daysover == 2:
        Day = "Tuesday" 
    if daysover ==3:
        Day = "Wednesday"
    if daysover == 4:
        Day = "Thursday"
    if daysover == 5:
        Day = "Friday" 
    if daysover == 6:
        Day = "Saturday"
    else:
        Day = "Sunday"
    return print(Day, timeofday)

    
    
    
    
    
