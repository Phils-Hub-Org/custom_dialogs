import os, sys
from PySide6.QtWidgets import QApplication

# To import Dialogs from this directory
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

from Dialogs.options_message_box import displayOptionsMessageBox

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    result = displayOptionsMessageBox('Options Message Box', ['Option 1', 'Option 2', 'Option 3'])
    print(f'Selected Option: {result}')

    sys.exit(0)