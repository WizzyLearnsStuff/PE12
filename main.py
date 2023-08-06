from math import sqrt

def count_div(n):
    ans = 1

    for i in range(2, int(sqrt(n)) + 1):
        c = 1
        while n % i == 0:
            c += 1
            n /= i
        ans *= c

    return ans

d = 0
n = 1
while d < 500:
    if n & 1: 
        d = count_div(n) * count_div(n // 2 + 1)
    else:
        d = count_div(n // 2) * count_div(n + 1)
    # d = count_div(n * (n + 1) // 2)

    n += 1
    print(n, d)
    
print(n * (n - 1) // 2)
