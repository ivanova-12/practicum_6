radius = 6.5
diametr = radius * 2
size1, size2 = map(int, input().split('x'))
if max(size1, size2) >= diametr:
    print('нет')
if max(size1, size2) < diametr and ((radius ** 2 - ((max(size1, size2) // 2) ** 2))**0.5) * 2 >= min(size1, size2):
    print('да')


