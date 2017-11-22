#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
"""
    roll
    Copyright (C) 2017  Ronaldo Nascimento <ronaldo1@users.sf.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Ronaldo Nascimento <sgtnasty@gmail.com>"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2017 by Ronaldo Nascimento"
__license__ = "GNU GENERAL PUBLIC LICENSE v3 http://www.gnu.org/licenses/gpl-3.0.txt"


import random
import sys
import json


DIEFACE = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
BLOCK = u'\u2610'


def print_chart(value, max):
    strng = ''
    for _ in range(value):
        strng = strng + BLOCK
    spaces = max - len(strng)
    if spaces > 0:
        for _ in range(spaces):
            strng = strng + '_'
    strng = '[' + strng + ']'
    return strng


def main(iterations):
    total = 0
    min = 18
    max = 0
    avg = 0.0
    for i in range(iterations):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        print(u'{}{}{}'.format(DIEFACE[a-1],DIEFACE[b-1],DIEFACE[c-1]),)
        ismax = ' '
        sm = a + b + c
        if (sm == 18):
            ismax = '\u2605'
        if sm < min:
            min = sm
        if sm > max:
            max = sm
        total = total + sm
        print('{:2} {} {}'.format(sm, print_chart(sm, 18), ismax))
    avg = float(total) / float(iterations)
    print('{} roll(s): min={}, avg={}, max={}, total={}'.format(
        iterations, min, avg, max, total))


if __name__ == '__main__':
    x = 10
    if (len(sys.argv) > 1):
        x = int(sys.argv[1])
    main(x)