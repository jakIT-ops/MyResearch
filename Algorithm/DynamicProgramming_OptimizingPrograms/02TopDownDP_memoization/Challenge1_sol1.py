# Solution 1: Simple recursion
def staircase(n, m):
    if n == 0:
        return 1
    ways = 0
    for i in range(1, m+1):
        # if steps remaining is smaller than the jump step, skip
        if i <= n:
            # recursive call with n i units lesser where i is the number of steps taken here
            ways += staircase(n-i, m)
    return ways

print(staircase(4, 2))