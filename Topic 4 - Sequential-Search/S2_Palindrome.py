# count how many palindrom between N and M

def palindrome(n):
    s = str(n)     # Convert the number to string
    r = s[::-1]    # Reverse the string
    return int(s) == int(r)  # Check if original and reversed are equal
def solve(n, m):
    cnt = 0
    for i in range(n, m+1):      # Loop from n to m (inclusive)
        if palindrome(i):        # If number is a palindrome
            cnt += 1             # Count it
    return cnt
N, M = map(int, input().split())
print(solve(N, M))

# 10 100 input
# 9 output