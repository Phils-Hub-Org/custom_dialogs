from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from Resources.UI.ui_input_message_box import Ui_InputMessageBox

class InputMessageBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_InputMessageBox()
        self.ui.setupUi(self)

        # Initialize the result attribute to store input text or None
        self.result = None

        # Connect the submit button to handle submission and dialog closure
        self.ui.submit_btn.clicked.connect(self.onSubmit)
        self.ui.cancel_btn.clicked.connect(self.onCancel)

    def setText(self, text: str):
        self.ui.msg_label.setText(text)

    def onSubmit(self):
        # Store the input text if provided, or keep None if empty
        text_input = self.ui.input_field.text().strip()
        self.result = text_input if text_input else None
        self.close()
    
    def onCancel(self):
        self.result = None
        self.close()

    def getResult(self):
        return self.result

def displayInputMessageBox(message: str) -> str | None:
    msgBox = InputMessageBox()
    msgBox.setText(message)
    msgBox.exec()

    # Retrieve and return the result from the dialog
    return msgBox.getResult()
