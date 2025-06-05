N = int(input())
S = list(map(int, input().split()))

def solve():
    S.sort()
    while len(S) > 0:
        mid = (len(S) - 1) // 2
        print(S[mid], end= " ")
        S.remove(S[mid])
    print()

solve()    

#sort and print median first one by one