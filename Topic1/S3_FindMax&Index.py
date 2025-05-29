n = 5
s = [100,100,30,10,500]
max = 10
cnt = 0
for i in s:
    if i > max:
        max = i
        cnt = s.index(i)
    else:
        pass
print(max, cnt)  # =============== O(N^2)

def max(n, s):
    maxn, maxi = s[0], 0
    for i in range (1, n):
        if maxn < s[i]:
            maxn, maxi = s[i], i
    return maxn, maxi
print(max(5, [10,20,30,40,50])) # =================== O(N)