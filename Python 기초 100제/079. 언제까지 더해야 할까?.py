n = int(input())
s = 0
l = []
for i in range (1,n + 1):
    s += i
    if n >= s:
        l.append(i)
print(l[-1])
