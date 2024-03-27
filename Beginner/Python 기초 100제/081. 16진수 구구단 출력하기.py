n = input()
n = int(n, 16)
for i in range(1,16):
    print('%X'%n, '*', '%X'%i, '=', '%X'%(n * i),sep = '')
