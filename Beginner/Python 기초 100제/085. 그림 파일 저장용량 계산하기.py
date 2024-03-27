w,h,b = input().split()
w = int(w)
h = int(h)
b = int(b)

display = w * h * b / 8 / 1024 / 1024
print(format(display, ".2f"),'MB')
