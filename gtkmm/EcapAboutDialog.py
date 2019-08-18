import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class EcapAboutDialog(Gtk.AboutDialog):
    def __new__(cls):
        try:
            builder = Gtk.Builder()
            builder.add_from_file("window.glade")
        except:
            print("Failed to load XML GUI file window.glade")
    
        about_dialog = builder.get_object("about_dialog")
        about_dialog.__class__ = EcapAboutDialog

        return about_dialog

