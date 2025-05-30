n = int(input('Enter n: '))
def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n -1)
print(fac(n))

#////////////////////////////////

n = int(input('Enter n: '))
result = 1
for i in range(1, n+1):
    if i <= 1:
        result *= 1
    else:
        result *= i
print(result)