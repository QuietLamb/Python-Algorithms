def prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    s = str(n)  
    r = s[::-1]    
    return int(s) == int(r)

def solve(n, m):
    cnt = 0
    for i in range(n, m+1):
        if palindrome(i) and prime(i):
            cnt += 1
    return cnt
N, M = map(int, input().split())
print(solve(N, M))