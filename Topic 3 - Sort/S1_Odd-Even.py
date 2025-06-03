n = input('Enter n: ').split()
m = [int(i) for i in n]

odd, even = [], []
for i in m:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
odd.sort()
even.sort(reverse= True)
print(" ".join(map(str, odd)))   # or print(*odd)
print(" ".join(map(str, even)))  # or print(*even)

#==================================================

import random

Seed, min, max, N = 2022, 10, 100, 8
random.seed(Seed)
S = random.sample(range(min, max), N)

print(S)
print(sorted(S))