# /////////////// Using Iteration
def binSearch(x, n, S):
    left, right = 0, n - 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if x == S[mid]:
            return cnt
        elif x < S[mid]:
            right = mid -1
        else:
            left = mid + 1
    return cnt
def solve(n, m, S, X):
    total = 0
    for i in range(m):
        total += binSearch(X[i], n, S)
    print(total)
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)

# /////////////// Using Recursive

def binSearch(left, right, x, S):
    if left > right:
        return 0
    else:
        mid = (left + right) // 2
        if x == S[mid]:
            return 1
        elif x < S[mid]:
            return 1 + binSearch(left, mid - 1, x, S)
        else:
            return 1 + binSearch(mid + 1, right, x, S)
def solve(n, m, S, X):
    total = 0
    for i in range(m):
        total += binSearch(0, n - 1, X[i], S)
    print(total)
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)