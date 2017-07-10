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
# Standard GTK libararies
#
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#
# Standard Python libraries
#
import os, re, subprocess

#
# Our own libraries are here
#
from lib import config


#------------------------------------------------------------------#
#                                                                  #
#                         Helper functions                         #
#                                                                  #
#------------------------------------------------------------------#

#
# Get our current distro
#
DISTRO = re.split("\t", subprocess.getoutput("/usr/bin/lsb_release --id"))[1]

#
# Is the current distro Raspbian?
#
def isRaspbian():
    return (DISTRO == "Raspbian")

#
# Load a button with callback
#
def getButton(builder, buttonId, callback):
    button = builder.get_object(buttonId)
    button.connect("clicked", callback)
    return button

#
# Set a button's callback
#
def setButtonCallback(builder, buttonId, callback):
    button = builder.get_object(buttonId)
    button.connect("clicked", callback)

#
# Load the glade file with builder
#
def loadBuilder(windowName):
    print("loadBuilder: Creating builder object")
    builder = Gtk.Builder()
    gname = os.path.join(config.RES, windowName.lower() + ".glade")
    print("loadBuilder: Loading " + gname)
    builder.add_from_file(gname)
    print("loadBuilder: done")
    return builder

#
# Load and image file
#
def loadImage(imageName):
    fname = os.path.join(config.IMG, imageName)
    return Gtk.Image.new_from_file(fname)

