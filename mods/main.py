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
# Our own imports are here
#
from lib import config, tools


#------------------------------------------------------------------#
#                                                                  #
#                         Main window class                        #
#                                                                  #
#------------------------------------------------------------------#
class MainWindow:

    def __init__(self, parentWindow, base):
        print("MainWindow: init")

        self.name = "Main"
        self.base = base
        self.parent = parentWindow
        self.builder = tools.loadBuilder(self.name)
        self.window = self.builder.get_object(self.name.lower()+"Window")
        self.window = self.builder.get_object("mainWindow")

        tools.setButtonCallback(self.builder, "navButton",   self.navCmd)
        tools.setButtonCallback(self.builder, "radioButton", self.radioCmd)
        tools.setButtonCallback(self.builder, "musicButton", self.musicCmd)
        tools.setButtonCallback(self.builder, "obd2Button",  self.obd2Cmd)


    def on_delete(self, widget, event):
        print ("on_delete MainWindow")

    def getWindow(self):
        return self.window

    def getName(self):
        return self.name

    def navCmd(self, widget):
        print("MainWindow: Activating navigaton program")

    def radioCmd(self, widget):
        print("MainWindow: Starting radio program")

    def musicCmd(self, widget):
        print("MainWindow: Starting music program")

    def obd2Cmd(self, widget):
        print("MainWindow: Starting OBD2 program")


