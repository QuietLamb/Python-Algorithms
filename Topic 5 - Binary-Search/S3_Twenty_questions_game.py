# ///////////// Using Iteration

# import random

# def solve(x, s, t):
#     left, right = s, t
#     while left < right:
#         print(left, right, end=" ")
#         mid = (left + right)// 2
#         print(f"Bigger than {mid}?", end=" ")
#         if (x > mid):
#             print("yes")
#             left = mid + 1
#         else:
#             print("no")
#             right = mid
#     print(f"Your X is {left}")
#     return left

# S, T = map(int, input().split())
# SEED = int(input())
# random.seed(SEED)
# X = random.randint(S, T)
# solve(X, S, T)

# ///////////// Using Recursion
import random

def solve(x, left, right):
    if left >= right:
        print(f"Your X is {left}.")
        return left
    else:
        mid = (left + right) // 2
        print(left, right, end= " ")
        print(f"Bigger than {mid}?", end= " ")
        if x > mid:
            print("Yes")
            return solve(x, mid + 1, right)
        else:
            print("No")
            return solve(x, left, mid)
        
S, T = map(int, input().split())
SEED = int(input())
random.seed(SEED)
X = random.randint(S, T)
solve(X, S, T)