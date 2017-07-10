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
import re, subprocess

#
# Our own stuff would be imported  here
#
#from lib import distro, ui
#from lib.config import Config
#from lib.main import MainWindow


#------------------------------------------------------------------#
#                                                                  #
#                         Helper functions                         #
#                                                                  #
#------------------------------------------------------------------#

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
# Get our current distro
#
DISTRO = re.split("\t", subprocess.getoutput("/usr/bin/lsb_release --id"))[1]

#
# Is the current distro Raspbian?
#
def isRaspbian():
    return (DISTRO == "Raspbian")


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
        self.window = base.builder.get_object(self.name.lower()+"Window")
        self.window = self.base.builder.get_object("mainWindow")

        setButtonCallback(base.builder, "navButton",   self.navCmd)
        setButtonCallback(base.builder, "radioButton", self.radioCmd)
        setButtonCallback(base.builder, "musicButton", self.musicCmd)
        setButtonCallback(base.builder, "obd2Button",  self.obd2Cmd)


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
        # Load the UI file
        #
        self.builder = Gtk.Builder()
        self.builder.add_from_file("example3.glade")

        #
        # Load the main windows 
        #
        self.window = self.builder.get_object("baseWindow")
        self.container   = self.builder.get_object("containerWindow")

        #
        # Adjust the decoration
        #
        self.window.set_title("LINDA")
        if isRaspbian():
            self.window.fullscreen()
            self.window.set_decorated(False)
        else:
            self.window.set_default_size(800, 480)

        #
        # Make sure we find out about the end times so we can clean up
        #
        self.window.connect("delete-event", self.onDeleteWindow)

        #
        # Connect the button to the callback handler
        #
        self.backButton  = getButton(self.builder, "backButton",  self.backCmd)
        self.setupButton = getButton(self.builder, "setupButton", self.setupCmd)
        self.volButton   = getButton(self.builder, "volButton",   self.volCmd)

        #
        # Load the main module window
        #
        self.mainModule = MainWindow(self.window, self)

        #
        # Update the screen
        #
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

#------------------------------------------------------------------#
#                                                                  #
#                     Main program starts here                     #
#                                                                  #
#------------------------------------------------------------------#
if __name__ == '__main__':
    BaseWindow()
    Gtk.main()
