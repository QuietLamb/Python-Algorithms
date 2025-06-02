def gcd(n, m):
    print(n, m)
    if m == 0 :
        return n
    else:
        return gcd(m, n % m)
print(gcd(1071, 1029))

###################################

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n
print(gcd(1071, 1029))