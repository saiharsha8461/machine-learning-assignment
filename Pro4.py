n = input("Enter the three number(provide space between them): ")
l = n.split()
if l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
    print("Sum is 0")
else:
    print(f'Sum is {int(l[0])+int(l[1])+int(l[2])}')
