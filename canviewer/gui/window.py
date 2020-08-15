# Import C
from canviewer.gui import GLADE_UI_PATH
from canviewer.gui import Gtk

from canviewer.gui.dialogs import AboutDialog


class MainWindow(Gtk.Window):
    def __new__(cls, *args, **kwargs):
        # Create Builder
        builder = Gtk.Builder()
        builder.add_from_file(GLADE_UI_PATH)

        # Get Window Widget
        window = builder.get_object("window")
        window.__class__ = cls

        # Initialize Components
        window.init_components(builder)

        # Initialize Signals
        window.init_signals()
        
        # Return MainWindow Widget
        return window


    def __init__(self):
        # Initialize super class
        super().__init__()


    def init_components(self, builder):
        # AboutDialog
        self.about_dialog = AboutDialog()


    def init_signals(self):
        pass


    def activate_menu_close(self, widget):
        Gtk.main_quit()


    def activate_menu_about(self, widget):
        self.about_dialog.run()
        self.about_dialog.hide() 
