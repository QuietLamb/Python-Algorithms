N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def madd(A, B):
    n, m = len(A), len(A[0])
    C= [[0] * m for _ in range (n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

def mprint(A):
    for i in range(len(A)):
        print(" ".join(map(str, A[i])))


C = madd(A, B)
mprint(C)