import os, sys
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)
from Dialogs.input_message_box import displayInputMessageBox

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    result = displayInputMessageBox('Enter a mew tooltip!')
    print(result)
    sys.exit(0)