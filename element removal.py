import sys

n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

cost = 0
for i in range(n):
    cost += a[i] * (i + 1)

print(cost)
