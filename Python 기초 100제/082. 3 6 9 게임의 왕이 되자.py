n = int(input())
my_list = []

for i in range(1,n + 1):
    if i % 3 == 0:
        my_list.append('X')
    else:
        my_list.append(str(i))
print((' ').join(my_list))
