import turtle
x1, y1 = map(int, input().split())
r1 = int(input())
x2, y2 = map(int, input().split())
r2 = int(input())
dist_of_centr = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)
turtle.penup()
turtle.home()
if r1 + r2 == dist_of_centr:
    turtle.write('окружности имеют внешнее касание')
elif abs(r1 - r2) == dist_of_centr:
    turtle.write('окружности имеют внутреннее касание')
elif r1 + r2 < dist_of_centr:
    turtle.write('окружность лежит одна вне другой, не касаясь')
elif dist_of_centr < max(r1, r2) - min(r1, r2):
    turtle.write('одна окружность лежит внутри другой, не касаясь')
elif max(r1, r2) - min(r1, r2) < dist_of_centr < max(r1, r2) + min(r1, r2):
    turtle.write('окружности пересекаются')
turtle.done()

