# n = int(input('Enter n: '))
# import time
# start = time.time()
# cnt = 0
# for i in range(1, n+1):
#     if (n%i == 0):
#         cnt += 1
# print(cnt) 
# end = time.time()
# print(f'solve time: {end - start}')  #==================== O(N)
import math
n = int(input('Enter n: '))
cnt = 0
sqrtn = int(math.sqrt(n))
for i in range(1, sqrtn + 1):
    if n % i == 0:
        cnt += 2
    elif sqrtn * sqrtn == n:
        cnt -= 1
print(cnt)                      
#=================== T(n) = sqrt(n) + 1 => O(sqrt(N))