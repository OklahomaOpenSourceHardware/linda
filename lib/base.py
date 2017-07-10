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
from lib import tools
from mods.main import MainWindow


#------------------------------------------------------------------#
#                                                                  #
#                         Base window class                        #
#                                                                  #
#------------------------------------------------------------------#
class BaseWindow:

    #
    # BaseWindow Class initialization
    #
    def __init__(self):

        #
        # Load the Glade file
        #
        self.builder = tools.loadBuilder("base")

        #
        # Load the main windows 
        #
        self.window = self.builder.get_object("baseWindow")
        self.overlay = self.builder.get_object("overlayWindow")
        self.container   = self.builder.get_object("containerWindow")

        #
        # Adjust the decoration
        #
        self.window.set_title("LINDA")
        if tools.isRaspbian():
            self.window.fullscreen()
            self.window.set_decorated(False)
        else:
            self.window.set_default_size(800, 480)

        #
        # Add the wallpaper
        #
        self.background = tools.loadImage("background.png")
        self.overlay.add(self.background)
        self.overlay.add_overlay(self.container)

        #
        # Make sure we find out about the end times so we can clean up
        #
        self.window.connect("delete-event", self.onDeleteWindow)

        #
        # Connect the button to the callback handler
        #
        self.backButton  = tools.getButton(self.builder, "backButton",  self.backCmd)
        self.setupButton = tools.getButton(self.builder, "setupButton", self.setupCmd)
        self.volButton   = tools.getButton(self.builder, "volButton",   self.volCmd)


        #
        # Load the main module window
        #
        self.mainModule = MainWindow(self.window, self)


        #
        # Setup the menu processing
        #
        self.appStack = list()
        self.setupActive = False
        self.menuLevel = 0
        self.currentMod = None

        self.appStack.append(self.mainModule)
        self.loadModule(self.mainModule)


    def loadModule(self, mod):
        print("Base: loading", mod.getName(), "module")
        if (self.currentMod != None): 
            self.container.remove(self.currentMod.getWindow())

        self.currentMod = mod

        print("Base: placing the window")
        window = mod.getWindow()
        self.container.put(window, 25,60)
        window.show_all()
        self.window.show_all()

    #
    # Called when the application close button it pressed
    #
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    #
    # Called when the back button is pressed
    #
    def backCmd(self, button):
        print("that's all folks!")
        Gtk.main_quit()

    #
    # Called when the volume button is pressed
    #
    def volCmd(self, button):
        print("process volume changes")

    #
    # Called when the setup button is pressed
    #
    def setupCmd(self, button):
        print("load the setup window")
