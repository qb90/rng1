#!/usr/bin/python
# -*- coding: utf-8 -*-
from part1 import generate


def main():
    print("""\
        1 - randomowe liczby
    """)
    print("Wyswietl : ")
    odp = int(input())
    if odp == 1:
        generate()
    else:
        print("Nie rozumiem")
    print()


main()
