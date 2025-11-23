numbers = []
for i in range(200+1):
    if i < 10:
        numbers.append(i)
    elif 10 <= i < 100:
        numbers.append(i//10)
        numbers.append(i % 10)
    else:
        numbers.append(i//100)
        numbers.append((i % 100)//10)
        numbers.append((i % 100) % 10)
n = int(input())
print(numbers[n - 1])

