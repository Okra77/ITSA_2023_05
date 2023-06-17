n = int(input())

points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

is_critical = [True] * n
for i in range(n):
    for j in range(n):
        if i != j:
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                is_critical[i] = False
                break
print(''.join('Y' if ic else 'N' for ic in is_critical))