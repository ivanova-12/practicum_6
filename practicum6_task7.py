n = int(input())
if n % 5 == 0 or n % 7 == 0:
    print('да')
else:
    if n % 5 != 2 and n % 7 != 5:
        print('нет')
    else:
        print('да')
