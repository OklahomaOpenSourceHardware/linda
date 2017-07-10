#!/usr/bin/env python3
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LINDA. If not, see <http://www.gnu.org/licenses/>.
#
#------------------------------------------------------------------#
#                                                                  #
#                    Declare our external stuff                    #
#                                                                  #
#------------------------------------------------------------------#

#
# Standard Python libraries
#
import os, sys


#------------------------------------------------------------------#
#                                                                  #
#                        Program Constants                         #
#                                                                  #
#------------------------------------------------------------------#

TOP = sys.path[0]
BIN = os.path.join(TOP, "bin")
LIB = os.path.join(TOP, "lib")
MOD = os.path.join(TOP, "mods")
RES = os.path.join(TOP, "resources")
IMG = os.path.join(RES, "images")

CFG_PATH = os.path.expanduser('~/.config/linda')


print("Config: TOP = '" + TOP + "'")
print("Config: BIN = '" + BIN + "'")
print("Config: LIB = '" + LIB + "'")
print("Config: MOD = '" + MOD + "'")
print("Config: RES = '" + RES + "'")
print("Config: IMG = '" + IMG + "'")

