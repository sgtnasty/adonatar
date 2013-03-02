#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
"""
    A die roller.
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
    def __init__(self, arg):
        super(Adonatar, self).__init__()
        self.arg = arg
        

def main():
    print("adonatar/" + __version__)

if __name__ == '__main__':
    main()