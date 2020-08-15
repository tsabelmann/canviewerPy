from canviewer.gui import GLADE_UI_PATH
from canviewer.gui import Gtk

class AboutDialog(Gtk.AboutDialog):
    def __new__(cls, *args, **kwargs):
        try:
            builder = Gtk.Builder()
            builder.add_from_file(GLADE_UI_PATH)
        except:
            print("Failed to load XML GUI file window.glade")
    
        about_dialog = builder.get_object("about_dialog")
        about_dialog.__class__ = cls

        return about_dialog

