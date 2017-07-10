#!/usr/bin/env python3


#
# Standard PyGTK import stuff
#
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



#
# Base window class
#
class Base:

    #
    # Base Class initialization
    #
    def __init__(self):

        #
        # Load the UI file
        #
        self.builder = Gtk.Builder()
        self.builder.add_from_file("example1.glade")

        #
        # Load the main window 
        #
        self.window = self.builder.get_object("window1")
        self.window.set_default_size(800, 480)        

        #
        # Make sure we find out about the end times so we can clean up
        #
        self.window.connect("delete-event", self.onDeleteWindow)

        #
        # Connect the button to the callback handler
        #
        self.helloButton = self.builder.get_object("helloButton")
        self.helloButton.connect("clicked", self.onButtonPressed)

        #
        # Show the main window 
        #
        self.window.show_all()

    #
    # Called when the application close button it pressed
    #
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    #
    # Called when the Hello button is pressed
    #
    def onButtonPressed(self, button):
        print("Hello World!")


#
# Main program starts here
#
if __name__ == '__main__':
    Base()
    Gtk.main()
