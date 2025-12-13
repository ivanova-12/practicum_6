import turtle as t
xl1, yl1 = map(int, input().split())
xr1, yr1 = map(int, input().split())
xl2, yl2 = map(int, input().split())
xr2, yr2 = map(int, input().split())
t.penup()
t.goto(xl1, yl1)
t.pendown()
t.forward(abs(xl1 - xr1))
t.right(90)
t.forward(abs(yl1 - yr1))
t.right(90)
t.forward(abs(xl1 - xr1))
t.right(90)
t.forward(abs(yr1 - yl1))
t.right(90)
t.penup()
t.goto(xl2, yl2)
t.pendown()
t.forward(abs(xl2 - xr2))
t.right(90)
t.forward(abs(yl2 - yr2))
t.right(90)
t.forward(abs(xl2 - xr2))
t.right(90)
t.forward(abs(yr2 - yl2))
t.penup()
t.home()
if (xl1 < xl2) and (xr1 >xr2) and (yl1 > yl2) and (yr1 < yr2):
    t.write('один прямоугольник лежит внутри другого, не касаясь')
elif (xl1 > xl2) and (xr1 < xr2) and (yl1 < yl2) and (yr1 > yr2):
    t.write('один прямоугольник лежит внутри другого, не касаясь')
elif (xr1 == xl2) or (xl1==xr2) or (yl1==yr2) or (yr2 == yl2):
    t.write('прямоугольники имеют касание')
elif (xr1 < xl2) or (yr1 > yl2) or (xl1 > xr2) or (yr2 > yl1):
    t.write('прямоугольники лежат вне друг друга, не касаясь')
else:
    t.write('прямоугольники имеют пересечение')
t.home()
t.done()




