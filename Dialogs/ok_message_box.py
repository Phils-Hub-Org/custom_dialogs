from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from Resources.UI.ui_ok_message_box import Ui_OKMessageBox

class OKMessageBox(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_OKMessageBox()
        self.ui.setupUi(self)

        self.ui.ok_btn.clicked.connect(self.close)
    
    def setText(self, text):
        self.ui.msg_label.setText(text)

def displayOkMessageBox(message: str) -> None:
    msgBox = OKMessageBox()
    msgBox.setText(message)
    msgBox.exec()