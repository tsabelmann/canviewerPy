# Import C
from canviewer.gui import GLADE_UI_PATH
from canviewer.gui import Gtk, GLib

# Import C
import can

# Import C
from collections import deque

# Import R
import random

# Import T
import time
import threading


def can_id_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if not treestore[treeiter].parent:
        value = treestore[treeiter][0]
        cell_renderer.set_property('text', f'{value : 08X}')
    else:
        cell_renderer.set_property('text', '') 

# def data_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
#     if not treestore[treeiter].parent:
#         value = treestore[treeiter][3]
#         cell_renderer.set_property('text', f'{value : 08X}')
#     else:
#         pass
#         # cell.set_property('markup', f'<span foreground='red'>{tree_model[iter][0]:08X}</span>')

def phys_unit_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if treestore[treeiter].parent:
        value = treestore[treeiter][4]
        cell_renderer.set_property('text', value) 
    else:
        cell_renderer.set_property('text', '') 

def format_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if not treestore[treeiter].parent:
        value = treestore[treeiter][5]
        if value:
            cell_renderer.set_property('text', 'Extended')
        else:
            cell_renderer.set_property('text', 'Standard') 
    else:
        cell_renderer.set_property('text', '') 

def interface_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if not treestore[treeiter].parent:
        value = treestore[treeiter][6]
        cell_renderer.set_property('text', f'{value}') 
    else:
        cell_renderer.set_property('text', '') 

def count_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if not treestore[treeiter].parent:
        value = treestore[treeiter][7]
        cell_renderer.set_property('text', f'{value}') 
    else:
        cell_renderer.set_property('text', '') 

def cycle_time_column_cell_data_func(tree_column, cell_renderer, treestore, treeiter, data):
    if not treestore[treeiter].parent:
        value = treestore[treeiter][8]
        cell_renderer.set_property('text', f'{value}') 
    else:
        cell_renderer.set_property('text', '') 

class TabBox(Gtk.Box):
    def __new__(cls, *args, **kwargs):
        builder = Gtk.Builder()
        builder.add_from_file(GLADE_UI_PATH)

        box = builder.get_object('box')
        box.__class__ = cls

        box.init_components(builder)
        box.init_treeview()
        box.init_signals()

        return box

    def __init__(self, label):
        # Label
        self._label = Gtk.Label(label=label)

        # Threading Indicator
        self._running = False

        # Threading Lock
        self._lock = threading.Lock()

        # CAN Deque
        self._deque = deque()

        # Dict
        self._messages = dict()

        # Dummy Data
        treeiter = self._treestore.append(None, [0xFF, 'Message 1', 'Variable 1', f'{0x1FF : 08X}', 'Ah', True, 'vcan0', 0, 1000])        
        self._treestore.append(treeiter, None)

    def init_components(self, builder):
        self._start_treeview_button : Gtk.ToolButton = builder.get_object('start_treeview_button')
        
        self._stop_treeview_button : Gtk.ToolButton = builder.get_object('stop_treeview_button')

        self._clear_treestore_button : Gtk.ToolButton = builder.get_object('clear_treestore_button')

        # Get TreeView
        self._treeview = builder.get_object('treeview')

        # Configure ToolButton
        self._start_treeview_button.set_sensitive(True)
        self._stop_treeview_button.set_sensitive(False)
        self._clear_treestore_button.set_sensitive(True)
    
    def init_treeview(self):
        #  Get TreeStore
        self._treestore = Gtk.TreeStore(int, # CAN-ID 0
                                        str, # Message 1
                                        str, # Variable 2
                                        str, # Data 3
                                        str, # Phys-Unit 4
                                        bool, # Format 5
                                        str, # Interface 6
                                        int, # Count 7
                                        int # Cycle-Time 8
                                        )
        
        # Set TreeStore to TreeView
        self._treeview.set_model(self._treestore)
        
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('CAN-ID', renderer, text=0)
        column.set_cell_data_func(renderer, can_id_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Message', renderer, text=1)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Variable', renderer, text=2)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Data', renderer, text=3)
        # column.set_cell_data_func(renderer, data_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Phys-Unit', renderer, text=4)
        column.set_cell_data_func(renderer, phys_unit_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Format', renderer, text=5)
        column.set_cell_data_func(renderer, format_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Interface', renderer, text=6)
        column.set_cell_data_func(renderer, interface_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Count', renderer, text=7)
        column.set_cell_data_func(renderer, count_column_cell_data_func)
        self._treeview.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Cycle-Time', renderer, text=8)
        column.set_cell_data_func(renderer, cycle_time_column_cell_data_func)
        self._treeview.append_column(column)
        
    def init_signals(self):
        self._start_treeview_button.connect('clicked', self.on_start_treeview_button_clicked)
        self._stop_treeview_button.connect('clicked', self.on_stop_treeview_button_clicked)
        self._clear_treestore_button.connect('clicked', self.on_clear_treestore_button_clicked)

    # Properties
    @property
    def label(self):
        return self._label

    def add_new_row(self, can_id, message, variable, data, phys_unit, format, interface, count, cycle_time):
        treeiter = self._treestore.append(None, [can_id, message, variable, data, phys_unit, format, interface, count, cycle_time])

        self._messages[can_id] = treeiter
        return False

    def update_new_row(self, treeiter):
        self._treestore[treeiter][7] += 1
        return False

    def render(self):
        while self._running:
            if self._deque:
                # intf = None
                # msg = None
                with self._lock:
                    intf, msg = self._deque.pop()

                if not msg.arbitration_id in self._messages:
                    value = int.from_bytes(msg.data, 'little')
                    GLib.idle_add(self.add_new_row, *[msg.arbitration_id, 'Message 1', 'Variable 1', f'{value : 08X}', 'Ah', msg.is_extended_id, intf, 0, 1000])  
                else:
                    treeiter = self._messages[msg.arbitration_id]
                    GLib.idle_add(self.update_new_row, treeiter)
                
            time.sleep(0.001)

    def receive_can(self):
        bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

        while self._running:
            msg = bus.recv(0.001)
            if msg:
                with self._lock:
                    self._deque.append(('vcan0', msg))

    # Signals
    def on_start_treeview_button_clicked(self, widget):
        self._start_treeview_button.set_sensitive(False)
        self._stop_treeview_button.set_sensitive(True)
        self._clear_treestore_button.set_sensitive(False)

        self._running = True

        thread0 = threading.Thread(target=self.receive_can)
        thread0.start()

        thread1 = threading.Thread(target=self.render)
        thread1.start()

    def on_stop_treeview_button_clicked(self, widget):
        self._running = False
    
        self._stop_treeview_button.set_sensitive(False)
        self._start_treeview_button.set_sensitive(True)
        self._clear_treestore_button.set_sensitive(True)

    
    def on_clear_treestore_button_clicked(self, widget):
        self._treestore.clear()
        self._messages = dict()
    