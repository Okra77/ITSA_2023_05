t = int(input())

for _ in range(t):
    n, m, l = map(int, input().split())
    points = set()
    for _ in range(l):
        x, y = map(int, input().split())
        points.add((x-1, y-1))
    all_points = set()
    for i in range(n):
        for j in range(m):
            all_points.add((i, j))
    for x, y in points:
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= i < n and 0 <= j < m:
                all_points.discard((i, j))
    if not all_points:
        print("Y")
    else:
        print("N")
