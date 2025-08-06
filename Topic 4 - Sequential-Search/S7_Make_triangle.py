#//////////////// Normal
# def solve(n):
#     cnt = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range (b, n):
#                 if a + b + c == n and a + b > c:
#                     cnt += 1
#     return cnt

#//////////////// Junior
# def solve(n):
#     cnt = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             c = n - a - b
#             if b <= c and a + b > c:
#                 cnt += 1
#     return cnt

#////////////////// Senior
def solve(n):
    cnt = 0
    for c in range((n+1) // 3, (n+1) // 2):
        cnt += c - (n-c+1) //2+1
    return cnt

N = int(input('Enter n: '))
print(solve(N))