a, b = map(int, input().split('x'))
c_dlina, d_shirina, e_visota = map(int, input().split('x'))
if min(c_dlina * e_visota, d_shirina * e_visota, d_shirina * c_dlina) <= a * b:
    print('да')
else:
    print('нет')
