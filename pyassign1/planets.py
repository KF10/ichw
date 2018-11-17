
"""planets.py: Description of the orbit of earth's six planets around the sun.

__author__ = "Kuangwenyu"
__pkuid__  = "1800013245"
__email__  = "w.y.kuang@pku.edu.cn"
"""

import math
import turtle

def t_elliptic_orbit(t, a, b, speed):
    """Make 't' move at a certain speed on an elliptic orbit with 'a' as semi-long axis and 'b' as semi-short axis.
    Unfortunately, the function is of practical use only in this program.
    """
    i = x // 6  # 在main module中会用x来构造一个循环使得六个行星同时在绕着太阳转
    degrees = 90 + i % 2000 *speed
    rad = degrees/180*math.pi
    t.goto(-a*math.sin(rad), b*math.cos(rad))
        
def main():
    """main module
    """
    wn = turtle.Screen()
    wn.setworldcoordinates(-300, -300, 300, 300)
    
    planets = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),
              turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
    colors = ['red', 'blue', 'gold', 'cornflowerblue', 'firebrick', 'yellowgreen', 'darkorange']
    c = 70  # 椭圆的半焦距
    a = [70, 100, 130, 160, 190, 220, 250]  # 行星的半长轴（第一个数仅用于占据第一个位置，无实际含义，下同）
    b = [math.sqrt(a[0]**2 - c**2), math.sqrt(a[1]**2 - c**2), math.sqrt(a[2]**2 - c**2),
         math.sqrt(a[3]**2 - c**2), math.sqrt(a[4]**2 - c**2), math.sqrt(a[5]**2 - c**2),
         math.sqrt(a[6]**2 - c**2)]  # 行星的半短轴
    speed = [0, 6, 5, 4, 3, 2, 1]  # 行星围绕太阳转的速度
    for i in range(7):
        planets[i].shape('circle')
        planets[i].color(colors[i])
        planets[i].speed(0)
        planets[i].pu()
        planets[i].goto(-a[i], 0)
        planets[i].pd()
        
    global x
    x = 1
    while True:
        i = x % 6
        if i != 0:
            t_elliptic_orbit(planets[i], a[i], b[i], speed[i])
        else:
            i = 6
            t_elliptic_orbit(planets[i], a[i], b[i], speed[i])
        x += 1
        
if __name__ == '__main__':
    main()
