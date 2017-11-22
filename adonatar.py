#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
"""
    Legend of the Adonatar
    Copyright (C) 2013  Ronaldo Nascimento <ronaldo1@users.sf.net>

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

__author__ = "Ronaldo Nascimento <ronaldo1@users.sf.net>"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 by Ronaldo Nascimento"
__license__ = "GNU GENERAL PUBLIC LICENSE v3 http://www.gnu.org/licenses/gpl-3.0.txt"

import random

class Adonatar(object):
    """docstring for Adonatar"""
    def __init__(self, name):
        super(Adonatar, self).__init__()
        self.name = name
        self.charisma = 0
        self.constitution = 0
        self.cunning = 0
        self.dexterity = 0
        self.power = 0
        self.perception = 0
        self.strength = 0
        self.willpower = 0
        self.level = 1
    def sheet(self):
        print('Hero: %s' % self.name)
        print('Attributes')
        print(' Charisma:     %d' % self.charisma)
        print(' Constitution: %d' % self.constitution)
        print(' Cunning:      %d' % self.cunning)
        print(' Dexterity:    %d' % self.dexterity)
        print(' Power:        %d' % self.power)
        print(' Perception:   %d' % self.perception)
        print(' Strength:     %d' % self.strength)
        print(' Willpower:    %d' % self.willpower)
        print('Level: 1')

def roll3d6():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def determine_attribute(attr):
    value = 0
    if (attr < 4):
        value = -3
    elif attr < 6:
        value = -2
    elif attr < 9:
        value = 0
    elif attr < 12:
        value = 1
    elif attr < 15:
        value = 2
    elif attr < 18:
        value = 3
    else:
        value = 4
    return value

def roll_attributes(pc):
    pc.charisma = determine_attribute(roll3d6())
    pc.constitution = determine_attribute(roll3d6())
    pc.cunning = determine_attribute(roll3d6())
    pc.dexterity = determine_attribute(roll3d6())
    pc.power = determine_attribute(roll3d6())
    pc.perception = determine_attribute(roll3d6())
    pc.strength = determine_attribute(roll3d6())
    pc.willpower = determine_attribute(roll3d6())

def main():
    print("adonatar/" + __version__)
    pc = Adonatar('unknown')
    roll_attributes(pc)
    pc.sheet()

if __name__ == '__main__':
    main()