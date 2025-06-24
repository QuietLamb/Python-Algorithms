#Exercise 1

def insert(n, s):
    cnt = 0
    for i in range(1, n):
        j, val = i - 1, s[i]
        cnt += 1
        while j>=0 and s[j]> val:
            s[j+1] = s[j]
            j -= 1
            cnt += 1
        s[j+1] = val
    return cnt
N = int(input())
S = list(map(int, input().split()))
print(insert(N, S))


# Exercise 2

def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: # Shift elements greater than key to the right 
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key # Place key at the right position

num = [5, 2, 4, 6, 1, 3]
insert(num)
print(num)   