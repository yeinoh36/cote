str = input()
for apb in str:
    if apb.isupper():
        print(apb.lower(), end='')
    elif apb.islower():
        print(apb.upper(), end='')
