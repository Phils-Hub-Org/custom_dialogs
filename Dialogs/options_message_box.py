from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QButtonGroup
from Resources.UI.ui_options_message_box import Ui_OptionsMessageBox

class OptionsMessageBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_OptionsMessageBox()
        self.ui.setupUi(self)

        # Initialize the result attribute to store input text or None
        self.result = None

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.option1, 1)
        self.button_group.addButton(self.ui.option2, 2)
        self.button_group.addButton(self.ui.option3, 3)

        # Connect the submit button to handle submission and dialog closure
        self.ui.submit_btn.clicked.connect(self.onSubmit)

    def setText(self, text: str):
        self.ui.msg_label.setText(text)
    
    def setOptions(self, options: list):
        self.ui.option1.setText(options[0])
        self.ui.option2.setText(options[1])
        self.ui.option3.setText(options[2])

    def onSubmit(self):
        # Retrieve the selected option from the button group
        selected_option = self.button_group.checkedId()

        # Store the selected option in the result attribute
        self.result = selected_option

        # Close the dialog
        self.close()

    def getResult(self):
        return self.result

def displayOptionsMessageBox(message: str, options: list) -> str | None:
    msgBox = OptionsMessageBox()
    msgBox.setText(message)
    msgBox.setOptions(options)
    msgBox.exec()

    # Retrieve and return the result from the dialog
    return msgBox.getResult()
