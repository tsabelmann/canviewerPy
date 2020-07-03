# Import G
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GLib, Pango, GObject

# Import O
import os

GLADE_UI_PATH = os.path.join( os.path.abspath( os.path.dirname(__file__) ), 'glade', 'window.glade')