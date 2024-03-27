n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
a = list(a)
a.sort()
a.pop(0)
