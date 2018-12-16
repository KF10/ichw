#!/usr/bin/env python3

"""tile.py:  Cover m*n(length and width) wall with a*b tiles

__author__ = "Kuangwenyu"
__pkuid__  = "1800013245"
__email__  = "w.y.kuang@pku.edu.cn"
"""

import turtle
import tkinter  

def tile(m, n, a, b, x):
    """There are x a*b tiles in the m*n wall.
    """
    tot = []    #建立墙所有位置的一维列表,编号从左到右，从上到下
    for i in range(m * n ):
        tot.append(i)
    tiles = []  #储存所有的砖块
    for i in range(m):
        for j in range(n):
            if i + a <= m and j + b <= n:
                lst =[]
                for c in range(a):
                    for d in range(b):
                        lst.append((j+d)*m + i + c)
                tiles.append(tuple(sorted(lst)))
            if i + b <= m and j + a <= n:
                lst =[]
                for c in range(b):
                    for d in range(a):
                        lst.append((j+d)*m + i + c)
                tiles.append(tuple(sorted(lst)))
    
    if 1 == x:    # 开始递归
        ways = [[tiles[0]], [tiles[1]]]
        return ways
    ways = []
    for i in tile(m ,n, a, b, x-1):   # i 是代表铺法的列表
        all_set = {0} # 用于储存所有已用了的瓷砖
        for j in i:
            for k in j:
                all_set.add(k)     
        for j in tiles:
            if set(j).isdisjoint(all_set):
                t = j[0]  # 找到一块还没被用的墙位
                break
            else:
                t =  0
        if t != 0:
            for j in tiles:
                part = i[:]
                if t in j and set(j).isdisjoint(all_set): #将可加入的且含有t的瓷砖加入到ways中
                    part.append(j)
                    ways.append(part)
             
    ways = set(tuple(sorted(i)) for i in ways)  #去掉重复的铺法
    ways = list(list(i) for i in ways)
    return ways  

def drawtile(t, x, y):
    """t draw a tile with length of x and width of y.
    """
    for i in range(4):
        if i % 2 == 0:
            t.fd(x)
            t.lt(90)
        else:
            t.fd(y)
            t.lt(90)
            
def main():
    """main module
    """
    m = int(input('请输入墙的长度：'))
    n = int(input('请输入墙的宽度：'))
    a = int(input('请输入瓷砖的长度：'))
    b = int(input('请输入瓷砖的宽度：'))
                
    result = tile(m, n, a, b, (m*n)/(a*b))
    print('铺法的总数：', len(result))
    print('所有的铺法：')
    
    for i in result:
        print(i)
        
    t = turtle.Turtle()
    t.speed(0)
    wn = turtle.Screen()
    wn.setworldcoordinates(-1, max(m,n)+1, max(m,n)+1, -1)
    num = tkinter.simpledialog.askinteger('Select plan', 'Input number of 0 - {0}'
                                          .format(len(result)-1))
    sel = result[num]
    for i in sel:
        cnt = 1
        for j in range(max(a,b)-1):
            if i[j+1] - i[j] == 1:
                cnt += 1
            else:
                break
        x = i[0] % m
        y = i[0] // m
        t.pu()
        t.goto(x, y)
        t.pd()
        if cnt == a:
            drawtile(t, a, b)
        else:
            drawtile(t, b, a)
            
if __name__ == '__main__':
    main()
        
