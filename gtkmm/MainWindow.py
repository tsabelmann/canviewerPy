import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gtkmm.TabBox import TabBox
from gtkmm.EcapAboutDialog import EcapAboutDialog

class MainWindow(Gtk.Window):
    def __new__(cls):
        try:
            builder = Gtk.Builder()
            builder.add_from_file("window.glade")
        except:
            print("Failed to load XML GUI file window.glade")
    
        # Get Window Widget
        window = builder.get_object("window")
        window.__class__ = MainWindow

        # Initialize Components
        window.init_components(builder)

        # Initialize Signals
        window.init_signals()
        
        # Return MainWindow Widget
        return window

    def init_components(self, builder):
        # AboutDialog
        self.about_dialog : EcapAboutDialog = EcapAboutDialog()

        # ToolButton
        self.remove_tab_button : Gtk.ToolButton = builder.get_object("remove_tab_button")
        self.add_tab_button : Gtk.ToolButton = builder.get_object("add_tab_button")

        # ToolEntry
        self.add_tab_entry : Gtk.Entry = builder.get_object("add_tab_entry")

        # Menu Items
        self.menu_close : Gtk.ImageMenuItem = builder.get_object("menu_close")
        self.menu_about : Gtk.ImageMenuItem = builder.get_object("menu_about")

        # Note Book
        self.notebook : Gtk.Notebook = builder.get_object("notebook")

    def init_signals(self):
        # Menu Items
        self.menu_close.connect("activate", self.activate_menu_close)
        self.menu_about.connect("activate", self.activate_menu_about)

        # ToolButton
        self.remove_tab_button.connect("clicked", self.remove_tab)
        self.add_tab_button.connect("clicked", self.add_tab)
        
        # ToolEntry
        self.add_tab_entry.connect("activate", self.add_tab)
    
    def activate_menu_close(self, widget):
        Gtk.main_quit()

    def activate_menu_about(self, widget):
        self.about_dialog.run()
        self.about_dialog.hide() 

    def remove_tab(self, widget):
        page = self.notebook.get_current_page()
        if page != -1:
            self.notebook.remove_page(page)

    def add_tab(self, widget):
        num = -1
        if self.add_tab_entry.get_text():
            tab  = TabBox()
            text = self.add_tab_entry.get_text()
            num  = self.notebook.insert_page(tab, Gtk.Label(text), -1)

        # if num != -1:
        #     page = self.notebook.get_nth_page(num)
        #     self.notebook.set_tab_reorderable(page, True)
        #     self.notebook.set_tab_detachable(page, True)
        

