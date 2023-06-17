T = int(input())
items = {}
total = 0
for i in range(T):
    product,s = input().split()
    s = int(s)
    items[product] = s
    total += s
sorted_items = sorted(items.items(), key=lambda x: x[0])

for product,s in sorted_items:
    ratio = s/total
    print(product,end="")
    print("({:.2f})".format(ratio))