# Import c
import click

from canviewer.gui import Gtk
from canviewer.gui.window import MainWindow


def main():
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()