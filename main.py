import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import json as js

def start_view_clicked(self):
    print(self)
    print("The start view button has been clicked")


builder = Gtk.Builder()
builder.add_from_file("window.glade")

#main_window
main_window = builder.get_object("main_window")
main_window.connect("destroy", Gtk.main_quit)

#start_view
start_view = builder.get_object("start_view")
start_view.connect("clicked", start_view_clicked)

#listview
listview = builder.get_object("listview")
store       = Gtk.ListStore(str, int, bool)

renderer    = Gtk.CellRendererText()
column      = Gtk.TreeViewColumn("interface", renderer, text=0)
listview.append_column(column)

renderer    = Gtk.CellRendererText()
column      = Gtk.TreeViewColumn("bitrate", renderer, text=1)
listview.append_column(column)

renderer    = Gtk.CellRendererToggle()
renderer.set_property("editable", True)
column      = Gtk.TreeViewColumn("active", renderer, text=2)

listview.append_column(column)

treeiter = store.append(["The Art of Computer Programming",
                         500000, False])

listview.set_model(store)

main_window.show_all()
Gtk.main()