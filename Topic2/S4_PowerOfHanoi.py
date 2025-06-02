def hanoi(n, src,via,dst):
    global cnt
    if n == 1:
        print(f'{src} -> {dst}')
        cnt += 1
    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1, src, via, dst)
        hanoi(n - 1, via, src, dst)
cnt = 0
hanoi(3, 'A','B','C')
print(cnt)
