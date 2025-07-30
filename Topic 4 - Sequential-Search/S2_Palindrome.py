# count how many palindrom between N and M

def palindrome(n):
    s = str(n)     # Convert the number to string
    r = s[::-1]    # Reverse the string
    return int(s) == int(r)  # Check if original and reversed are equal
def solve(n, m):
    cnt = 0
    for i in range(n, m+1):
        if palindrome(i):
            cnt += 1
    return cnt
N, M = map(int, input().split())
print(solve(N, M))

# 10 100 input
# 9 output