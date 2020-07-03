from canviewer.gui import GLADE_UI_PATH
from canviewer.gui import Gtk

class TabBox(Gtk.Box):
    def __new__(cls, *args, **kwargs):
        builder = Gtk.Builder()
        builder.add_from_file(GLADE_UI_PATH)

        box = builder.get_object("box")
        box.__class__ = cls

        box.init_components(builder)
        box.init_signals()

        return box

    def init_components(self, builder):
        # Init Class Variables
        self.is_recording = False

        self.start_treeview : Gtk.ToolButton = builder.get_object("start_treeview")
        self.stop_treeview : Gtk.ToolButton = builder.get_object("stop_treeview")

        self.start_recording : Gtk.ToolButton = builder.get_object("start_recording")
        self.stop_recording : Gtk.ToolButton = builder.get_object("stop_recording")

        # Configure ToolButton
        self.stop_treeview.set_sensitive(False)
        self.start_recording.set_sensitive(False)
        self.stop_recording.set_sensitive(False)

    def init_signals(self):
        self.start_treeview.connect("clicked", self.on_start_treeview_clicked)
        self.stop_treeview.connect("clicked", self.on_stop_treeview_clicked)

        self.start_recording.connect("clicked", self.on_start_recoring_clicked)
        self.stop_recording.connect("clicked", self.on_stop_recording_clicked)

    def on_start_treeview_clicked(self, widget):
        self.start_treeview.set_sensitive(False)
        self.stop_treeview.set_sensitive(True)
        self.start_recording.set_sensitive(True)

    def on_stop_treeview_clicked(self, widget):
        self.stop_treeview.set_sensitive(False)
        self.start_treeview.set_sensitive(True)

        if self.is_recording:
            self.on_stop_recording_clicked(widget)
        
        self.start_recording.set_sensitive(False)
        self.stop_recording.set_sensitive(False)
        
    def on_start_recoring_clicked(self, widget):
        self.is_recording = True

        self.start_recording.set_sensitive(False)
        self.stop_recording.set_sensitive(True)

    def on_stop_recording_clicked(self, widget):
        self.is_recording = False

        self.stop_recording.set_sensitive(False)
        self.start_recording.set_sensitive(True)