
# printing square pattern

# getting input from the user
r = int(input('enter the row: '))

# performing 'for' loop
# intialising row
for i in range(r):
    # intialising column
    for j in range(r):
        print('$', end = ' ')
    # print for next line
    print()