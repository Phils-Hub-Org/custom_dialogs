from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from Resources.UI.ui_yes_no_message_box import Ui_YESNOMessageBox

class YesNoMessageBox(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_YESNOMessageBox()
        self.ui.setupUi(self)

        self.ui.yes_btn.clicked.connect(self.accept)
        self.ui.no_btn.clicked.connect(self.reject)
    
    def setText(self, text):
        self.ui.msg_label.setText(text)

def displayYesNoMessageBox(message: str) -> bool:
    msgBox = YesNoMessageBox()
    msgBox.setText(message)
    result = msgBox.exec()  # This will return QDialog.Accepted or QDialog.Rejected
    return result == QDialog.Accepted  # Returns True if "Yes" is clicked, False otherwise
