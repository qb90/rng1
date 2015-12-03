#!/usr/bin/python
# -*- coding: utf-8 -*-


def count(p):
    counter = 0
    e = []
    l = len(p)
    for i in range(l):
        if p[i] in e:
            counter += 1
        else:
            e.append(p[i])
    le = len(e)
    print('repeated points :', le)
    pt = 2500 - le
    del e
    return pt
