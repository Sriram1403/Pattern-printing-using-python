
r = int(input('enter the row: '))

for i in range(r):
    for j in range(r-i):
        print('$', end= ' ')
    print()