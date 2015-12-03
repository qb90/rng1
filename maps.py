#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
from random import randrange
import datetime
from pointctr import count
from colorchk import check


def drawimage():
    for u in range(100):
        tmp = []
        for j in range(2500):
            x = 0
            tmp.append(x)
        c = []
        p = []
        im = Image.new(mode="RGB", size=(50, 50), color=(0, 0, 0))
        draw = ImageDraw.Draw(im)
        for i in range(15000):
            r = g = b = 255
            x = randrange(50)
            y = randrange(50)
            xy = (x, y)
            ch = check(c, tmp, xy)
            if ch <= 9:
                r = 255 - ch*30
            elif ch > 9:
                g = 255 - ch*30
            draw.point(xy=[xy], fill=(r, g, b))
            p.append(xy)
        score = count(p)
        date = '{:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
        d = date
        name = 'img/image_color/%s_map_%d_empty_%d.png' % (d, u, score)
        im.save(name)
        print('Generated :', name)
        del draw
        del p
        del c
        del tmp
    print()