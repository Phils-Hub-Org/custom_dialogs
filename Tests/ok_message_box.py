import os, sys
from PySide6.QtWidgets import QApplication

# To import Dialogs from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from Dialogs.ok_message_box import displayOkMessageBox

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    displayOkMessageBox('Hello World!')
    
    sys.exit(0)