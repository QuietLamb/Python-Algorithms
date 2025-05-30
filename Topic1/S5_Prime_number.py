# n = int(input('Enter: '))
# import time 
# start = time.time()
# x = 1
# for i in range (2, n):
#     if n%i == 0:
#         print(f"{n} is not a prime number")
#         x -= 1
#         break
# end = time.time()
# if x == 1:
#     print(f"{n} is prime number")
# end = time.time() 
# print('time', end - start)   #========================== O(N)

import math
n = int(input("Enter n: "))
import time
start = time.time()
sqrtn = int(math.sqrt(n))
def solve(n):
    for i in range (2, sqrtn + 1):
        if n % i == 0:
            return False
    return True
print('yes' if solve(n) else 'no')
end = time.time()
print(f"time: ",end - start)         #===================



    