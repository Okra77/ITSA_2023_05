import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    m = k + 1
    while True:
        flag = True
        pos = 0
        for i in range(k):
            pos = (pos + m - 1) % (2 * k - i)
            if pos < k:
                flag = False
                break
            pos -= k
        if flag:
            print(m)
            break
        m += gcd(2 * k, m)
