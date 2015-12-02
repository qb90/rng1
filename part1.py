#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange


def random():
    for j in range(10):
        rnd = randrange(1000)
        print('Wygenerowano :', rnd)
    print()
