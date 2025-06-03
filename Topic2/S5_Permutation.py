def perm(i, n, s):
    if i == n - 1:
        print("".join(s)) # remove "" from S
    else:
        for j in range(i, n):
            s[i], s[j] = s[j], s[i] #swap
            perm(i+1, n, s)
            s[i], s[j] = s[j], s[i] #swap

N = int(input())
S = [chr(ord('A') + i) for i in range(N)]
perm(0, N, S)