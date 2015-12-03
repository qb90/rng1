#!/usr/bin/python
# -*- coding: utf-8 -*-


def check(c, tmp, xy):
    if xy in c:
        i = c.index(xy)
        tmp[i] = tmp[i] + 1
        counter = tmp[i]
    else:
        c.append(xy)
        i = c.index(xy)
        tmp[i] = 1
        counter = tmp[i]
    return counter
