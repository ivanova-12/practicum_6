letters_1 = 'aceg'
letters_2 = 'bdfh'
n = input()
if n[0] in letters_1 and int(n[1]) % 2 == 0:
    print('белый')
elif n[0] in letters_1 and int(n[1]) % 2 == 1:
    print('черный')
elif n[0] in letters_2 and int(n[1]) % 2 == 0:
    print('черный')
elif n[0] in letters_2 and (int(n[1])) % 2 == 1:
    print('белый')

