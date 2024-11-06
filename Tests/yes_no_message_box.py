import os, sys
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)
from Dialogs.yes_no_message_box import displayYesNoMessageBox

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    result = displayYesNoMessageBox('Would you like to exit?')
    print(result)
    sys.exit(0)