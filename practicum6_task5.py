def cletka(n):
    letters_1 = 'aceg'
    letters_2 = 'bdfh'
    if n[0] in letters_1 and int(n[1]) % 2 == 0:
        res = 'белый'
    elif n[0] in letters_1 and int(n[1]) % 2 == 1:
        res = 'черный'
    elif n[0] in letters_2 and int(n[1]) % 2 == 0:
        res = 'черный'
    elif n[0] in letters_2 and (int(n[1])) % 2 == 1:
        res = 'белый'
    return res

str_of_all_letters = 'abcdefgh'
n1, n2 = input().split('-')
if int(n2[1]) == int(n1[1]) or int(n2[1]) == int(n1[1]) + 2 or int(n2[1]) == int(n1[1]) - 2 or int(n2[1]) == int(n1[1]) - 1 or int(n2[1]) == int(n1[1]) + 1:
    if cletka(n1) != cletka(n2) and abs(str_of_all_letters.find(n1[0]) - str_of_all_letters.find(n2[0])) <= 2:
        print('верно')
    else:
        print('oшибка')
else:
    print('ошибка')

