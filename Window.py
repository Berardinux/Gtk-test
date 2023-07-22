#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ui_layout import UiLayout

ui_layout = UiLayout()
ui_layout.connect("destroy", Gtk.main_quit)
ui_layout.show_all()
Gtk.main()