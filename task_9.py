import math
import turtle as t


def sector(x, y, r, ang, col):
    '''
    Function, drawing sector of pie.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param r: radius of  pie
    :param ang: angle of a sector of pie
    :param col: colour of the sector
    :return: None
    '''
    t.fillcolor(col)
    t.begin_fill()
    t.color(col)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(r)
    t.left(90)
    t.circle(r, ang)
    t.left(90)
    t.forward(r)
    t.end_fill()
    t.left(180-ang)


def draw_a(x, y, a):
    '''
    Function, drawing A.
    :param x: upper corner coordinate x
    :param y: upper corner coordinate y
    :param a: side of a letter
    :return: None
    '''
    t.color('black')
    t.up()
    t.setposition(x, y)
    t.down()
    t.right(70)
    t.forward(a)
    t.setposition(x, y)
    t.right(40)
    t.forward(a)
    t.up()
    t.setposition(x-a*math.sin(20)/4, y-a*math.cos(20))
    t.down()
    t.left(110)
    t.forward(a*math.sin(20)/2)


def draw_b(x, y, a):
    '''
    Function, drawing B.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side of a letter
    :return: None
    '''
    t.color('black')
    t.up()
    t.setposition(x, y)
    t.down()
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a/4)
    t.circle(a/4, 180)
    t.forward(a/4)
    t.right(180)
    t.forward(a/4)
    t.circle(a/4, 180)
    t.forward(a/4)
    t.right(180)


def draw_c(x, y, r):
    '''
    Function, drawing C.
    :param x: upper right corner coordinate x
    :param y: upper right corner coordinate y
    :param r: radius of a letter
    :return: None
    '''
    t.color('black')
    t.up()
    t.setposition(x, y)
    t.down()
    t.left(120)
    t.circle(r, 300)
    t.right(60)


def draw_d(x, y, a):
    '''
    Function, drawing D.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: height of a letter
    :return: None
    '''
    t.color('black')
    t.up()
    t.setposition(x, y)
    t.down()
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a/4)
    t.circle(a/2, 180)
    t.forward(a/4)
    t.right(180)


def draw_e(x, y, a):
    '''
    Function, drawing E.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: height of a letter
    :return: None
    '''
    t.color('black')
    t.up()
    t.setposition(x, y)
    t.down()
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a/2)
    t.up()
    t.setposition(x, y-a/2)
    t.down()
    t.forward(a/2)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a/2)


def main():
    '''
    Main function.
    :return: None
    '''
    t.left(90)
    sector(0, 1, 200, 21, 'dark blue')
    t.left(21)
    sector(-1, 0, 200, 42, 'green')
    t.left(42)
    sector(-2, -1, 200, 70, 'orange')
    t.left(70)
    sector(0, -2, 200, 105, 'red')
    t.left(105)
    sector(2, -0.5, 200, 122, 'blue')
    t.left(32)
    draw_a(190, 140, 10)
    draw_b(20, -220, 10)
    draw_c(-220, -20, 5)
    draw_d(-150, 170, 10)
    draw_e(-40, 220, 10)


main()
