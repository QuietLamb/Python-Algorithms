m = 0
def Count(n):
    global m
    while m != n+1:
        print(m)
        m += 1
        Count(n)
Count(20)