#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import argparse
from gtkmm.MainWindow import MainWindow

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()