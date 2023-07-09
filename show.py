#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def main():
    
    with open("./hyakunin.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]
    wakes = [s.strinp() for s in f.readline()]
    print(wakas[random.randrange(len(wakas))])
    
if __name__ == '__main__':
    main()