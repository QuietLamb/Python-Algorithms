#//////// Using Recursion

# def binSearch(left, right, x, S):
#     if left > right :
#         return -1
#     else:
#         mid = (left + right) // 2
#         if S[mid] == x:
#             return mid
#         elif x < S[mid]:
#             return binSearch(left, mid-1, x, S)
#         else:
#             return binSearch(mid+1, right, x, S)
# def solve(N, M, S, X):
#     for i in range(M):
#         j = binSearch(0, N-1, X[i], S) 
#         # N-1 : because if N = 10 so index only 0-9
#         print(j, end = " ")
#     print()

# N, M = map(int, input().split())
# S = list(map(int, input().split()))
# X = list(map(int, input().split()))
# solve(N, M, S, X)

# ///////////// Using Iteration

def binSearch(x, n, S):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
def solve(N, M, S, X):
    for i in range(M):
        j = binSearch(X[i], N, S)
        print(j, end=" ")
    print()
    
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)

