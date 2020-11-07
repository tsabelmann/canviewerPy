"""Module contains the code for the MainWindow widget.
"""

# Import C
from canviewer.ui import UI_PATH

# Import P
import pathlib

# Import P
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader

# PATHS
WINDOW_PATH = UI_PATH.joinpath(pathlib.Path("mainwindow.ui")).resolve()


class MainWindow(QtCore.QObject):
    def __init__(self):
        super().__init__()

        # Loader
        loader = QUiLoader()
        self.ui = loader.load(str(WINDOW_PATH), None)

        # # Data
        # self.data = dict()
        #
        # # Label DateTime
        # self.on_update_datetime()
        #
        # # Timer
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(1000)
        # self.timer.timeout.connect(self.on_update_datetime)
        # self.timer.start()
        #
        # # Actions
        # self.ui.actionSave.triggered.connect(self.on_save)
        # self.ui.actionClear.triggered.connect(self.on_clear)
        # self.ui.actionQuit.triggered.connect(self.on_quit)
        # self.ui.actionAddTextAndClear.triggered.connect(self.on_add_text_and_clear)
        # self.ui.actionAddTextAndKeep.triggered.connect(self.on_add_text_and_keep)
        #
        # # Signal
        # self.ui.pushButton.clicked.connect(self.on_add_button_clicked)

        # Show UI
        self.ui.show()
