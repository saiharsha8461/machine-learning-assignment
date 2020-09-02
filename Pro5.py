s = input("Enter the string: ").lower()
d = dict()
for l in s:
    d[l] = d.get(l, 0)+1
print("Occurance of characters in a string")
for k, v in d.items():
    print(f'{k}-{v}')
