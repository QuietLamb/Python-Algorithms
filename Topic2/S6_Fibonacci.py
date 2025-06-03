# def fib(n):
    
#     if (n == 1 or n == 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(1, 16):
#     print(fib(i))           #O(2^n)

########################################

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(3, n+1):
            a, b = b, a+b
        return b
print(fib(1000))        #O(n)