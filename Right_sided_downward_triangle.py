

r = int(input('enter the row: '))

for i in range(r):
    for j in range(i+1):
        print(' ', end= ' ')
    for j in range(i,r):
        print("$", end= ' ')
    print()