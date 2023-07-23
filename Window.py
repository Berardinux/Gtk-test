#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class UiLayout(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Blank GTK Window")

        self.set_default_size(500, 800)
        self.set_resizable(False)

        # Grid
        grid = Gtk.Grid()
        self.add(grid)

        # Other

        # Create an AspectFrame for the image
        image_frame = Gtk.AspectFrame(
            label="DTOS Hub",
            xalign=0.5,
            yalign=0.5,
            ratio=16/9,
            obey_child=True
        )

        image = Gtk.Image.new_from_file("Images/background.png")
        image_frame.add(image)

        # Create a vertical box for the image frame and label
        self.image_label_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.image_label_box.pack_start(image_frame, True, True, 0)

        label1 = Gtk.Label(label="Welcome to DTOS! Need help using DTOS or customizing it?")
        label1.set_hexpand(True)
        label2 = Gtk.Label(label="Or maybe you just want to learn more about Linux? We've got you covered.")
        label2.set_hexpand(True)

        self.image_label_box.pack_start(label1, True, True, 0)
        self.image_label_box.pack_start(label2, True, True, 10)

        # Create a horizontal box for the buttons
        buttons_box = Gtk.Box(spacing=0)
        button1 = Gtk.Button(label="About DTOS")
        button1.connect("clicked", self.on_button1_clicked)
        button2 = Gtk.Button(label="Knowledge Base")
        buttons_box.pack_start(button1, True, True, 10)
        buttons_box.pack_start(button2, True, True, 10)

        # Add the containers to the grid
        grid.attach(self.image_label_box, 0, 0, 2, 1)
        grid.attach(buttons_box, 0, 1, 2, 1)  # Span 2 columns for buttons

        # New Grid for Switches
        new_grid = Gtk.Grid()
        new_grid.set_margin_top(10)
        new_grid.set_margin_start(10)
        grid.attach(new_grid, 0, 2, 2, 1)

        # Create a vertical box for the switches
        switch_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        switch = Gtk.Switch()
        switch_box.pack_start(switch, True, True, 0)

        # Add the switch_box to the new grid
        new_grid.attach(switch_box, 0, 0, 1, 1)

    def __del__(self):
        self.destroy()

    def on_button1_clicked(self, button1):
        # Function to create and show a new window when label1 is clicked
        new_window = Gtk.Window(title="New Window")
        new_window.set_default_size(500, 800)
        self.set_resizable(False)

        label_in_new_window = Gtk.Label(label="This is a new window!")
        new_window.add(label_in_new_window)

        new_window.show_all()

        self.hide()    

ui_layout = UiLayout()
ui_layout.connect("destroy", Gtk.main_quit)
ui_layout.show_all()
Gtk.main()
