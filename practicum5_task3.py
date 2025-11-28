number = int(input())
number2 = number
rez = 0
while number > 0:
    letter = number % 10
    rez = rez * 10 + letter
    number //= 10
if rez == number2:
    print('настоящее')
else:
    print('кривое')
