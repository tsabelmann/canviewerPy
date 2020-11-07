# Import G
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GLib, Pango, GObject

# Import O
import os

# Paths
GLADE_UI_PATH = os.path.join( os.path.dirname(__file__), 'glade', 'window.glade')
CSS_PATH = None