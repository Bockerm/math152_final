# Use this file to write the various functions
# Try to write them from scratch

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