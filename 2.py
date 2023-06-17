def split_items(items):
    n = len(items)
    dp = [[0 for _ in range(n+1)] for _ in range(sum(items)//2+1)]
    for i in range(1, sum(items)//2+1):
        for j in range(1, n+1):
            if items[j-1] > i:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-items[j-1]][j-1] + items[j-1])
    i = sum(items)//2
    j = n
    items1 = []
    items2 = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            items1.append(j-1)
            i -= items[j-1]
            j -= 1
    items2 = [i for i in range(n) if i not in items1]
    return items1, items2



N = int(input())
a = list(map(int,input().split()))
a.sort()
items1, items2 = split_items(a)

print(abs(sum([a[i] for i in items1])-sum([a[i] for i in items2])))
