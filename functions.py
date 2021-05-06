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
        
        
        
#Fermat Little's Theorem states that if p is a prime number, then for any integer a, the number a^p – a is an integer multiple of p. 
#First, we check is the input is prime by using Wilson's Theorem which states a natural number p > 1 is a prime number if (p - 1) ! ≡  -1 mod p 

def isprime(j):
    (j-1) != -1 % j

def fermatlittle(prime, a):
    if isprime(prime):
        compute = a ** prime - a
        return ((compute % prime) == 0)
    else:
        return ("Input was not a prime number")
    
# assumming you start off the week on a Sunday
def clockarithmetic (hours):
    timeofday = hours%24
    fulldays = (hours-timeofday)/24
    daysover = fulldays%7
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

    
    
    
    
    
