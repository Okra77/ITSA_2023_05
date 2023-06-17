A = [1,1]
for i in range(1,21):
    sum = A[i-1]+A[i]
    A.append(sum)



T = int(input())

for i in range(T):
    n = int(input())
    print(A[n])