#!/usr/bin/python
# -*- coding: utf-8 -*-
from part1 import generate
from maps import drawimage


def main():
    print("""\
        1 - Several randoms
        2 - 50px x 50px maps
    """)
    print("Print : ")
    odp = int(input())
    if odp == 1:
        generate()
    elif odp == 2:
        drawimage()
    else:
        print("Not found")
    print()


main()
