import math
import turtle as t


def rounded_rectangle(x, y, a, r, col):
    '''
    Function, drawing rectangle with rounded angles.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param a: length of figure
    :param r: half a width of figure
    :param col: colour of the figure
    :return: None
    '''
    t.fillcolor(col)
    t.begin_fill()
    t.color(col)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.circle(r, 180)
    t.forward(a)
    t.circle(r, 180)
    t.end_fill()


def blue_circle(x, y, r):
    '''
    Function, drawing blue circle.
    :param x: lower corner coordinate x
    :param y: lower corner coordinate x
    :param r: radius of circle
    :return: None
    '''
    t.fillcolor('blue')
    t.begin_fill()
    t.color('blue')
    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(r)
    t.end_fill()


def main():
    '''
    Main function.
    :return: None
    '''
    rounded_rectangle(-150, -10, 300, 10, 'light blue')
    rounded_rectangle(-150-50*math.tan(math.radians(30)), 50, 300+2*50*math.tan(math.radians(30)), 10, 'light blue')
    t.left(90)
    rounded_rectangle(5, -50, 150, 10, 'light blue')
    t.left(15)
    rounded_rectangle(-55, -50, 150/math.cos(math.radians(15)), 10, 'light blue')
    t.left(15)
    rounded_rectangle(-140+25*math.tan(math.radians(30)), -25, 150/math.cos(math.radians(30)), 10, 'blue')
    t.left(60)
    rounded_rectangle(-130*math.tan(math.radians(30))-150, 130, 40, 10, 'blue')
    t.right(105)
    rounded_rectangle(65, -50, 150/math.cos(math.radians(15)), 10, 'light blue')
    t.right(15)
    rounded_rectangle(100+55*math.tan(math.radians(30)), -55, 150/math.cos(math.radians(30)), 10, 'blue')
    t.right(60)
    rounded_rectangle(-150-95*math.tan(math.radians(30)), 95, 300+2*100*math.tan(math.radians(30)), 10, 'blue')
    rounded_rectangle(-150+50*math.tan(math.radians(30)), -65, 300-2*50*math.tan(math.radians(30)), 10, 'blue')
    t.right(60)
    rounded_rectangle(-160+50*math.tan(math.radians(30)), -65, 25, 10, 'blue')
    t.left(60)
    rounded_rectangle(-150+50*math.tan(math.radians(30))+25*math.sin(math.radians(30)),
                      -75-25*math.cos(math.radians(30)), 300-125*math.tan(math.radians(30)), 10, 'blue')
    blue_circle(-60, -155, 25)
    blue_circle(60, -155, 25)


main()
