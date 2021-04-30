# Use this file to write the various functions
# Try to write them from scratch

<<<<<<< HEAD
def test():
    print('yo')
    
gcd = 0
def euclidean():
    a = int(input("Enter No.1"))
    b = int(input("Enter No.2"))
    r = a%b
    q = int(a/b)
    while(r!=0):
        a = b
        b = r
        q = int(a/b)
        r = a - (b * q)
    gcd = b
    print(b)

#test, should be 17 with 57970, 10353
euclidean()


def ext_euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = ext_euclid(b % a, a)
        return gcd, y - (b // a) * x, x

#test, should be 17, 302, -1691 for 57970, 10353
ext_euclid(57970, 10353)
=======
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


>>>>>>> 4f0ed68748a7f5ee3d67f6c06e938febd5d8ab46
