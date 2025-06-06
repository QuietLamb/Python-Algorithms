#=============== First approch =============

S = [(3,5), (2,1), (5,3), (1,4), (4,2)]
def first(k):
    return k[0]
def second(k):
    return k[1]
print(sorted(S, key= first))
print(sorted(S, key= second))

#=============== Second approch =============

S = [(3,5), (2,1), (5,3), (1,4), (4,2)]
print(sorted(S, key= lambda k: k[0]))
print(sorted(S, key= lambda k: k[1]))
print(sorted(S, key= lambda k: (k[0], -k[1])))

#=============== Combine (first approch) =============

S = [(2,5), (2,1), (1,3), (1,4), (1,2)]
print(sorted(S, key = lambda k: (k[0], k[1]))) #accending (second element)
print(sorted(S, key = lambda k: (k[0], k[1]))) #Decending (second element)

#=============== Combine (first approch) =============

S = [(2,5), (2,1), (1,3), (1,4), (1,2)]
S.sort(key = lambda k: (k[0], k[1]))
print(S)         #accending (second element)
S.sort(key = lambda k: (k[0], -k[1]))
print(S)         #Decending (second element)

#=============== Improving Code =============

def solve(n, p):
    P.sort(key = lambda x: (x[0], -x[1]))
    for i in range(n):
        print(" ".join(map(str, p[i])))

N = int(input())
P = [list(map(int, input().split())) for i in range(N)] 
solve(N,P)

#input example:
# 5
# 1 -1
# 2 3
# 4 -4