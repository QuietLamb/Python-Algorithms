def prime(N, M):
    for i in range(N+1, M):
        n = 1
        for j in range(2, i):
            if i % j == 0:
                n = 0
        if n == 1:
            print(i)
prime(12, 24)