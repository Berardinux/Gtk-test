#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class UiLayout(Gtk.Window):
        def __init__(self):
                Gtk.Window.__init__(self, title="Blank GTK Window")

                self.set_default_size(400, 600)

                # Grid
                grid = Gtk.Grid()
                self.add(grid)
        
                # Other
                image = Gtk.Image.new_from_file("Images/background.png")
                label1 = Gtk.Label(label="Label 1")
                label2 = Gtk.Label(label="Label 2")
                button1 = Gtk.Button(label="Button 1")
                button2 = Gtk.Button(label="Button 2")

                grid.attach(image, 0, 0, 3, 2)
                grid.attach(label1, 1, 2, 1, 1)
                grid.attach(label2, 0, 2, 1, 1)
                grid.attach(button1, 0, 3, 1, 1)
                grid.attach(button2, 1, 3, 1, 1)
        