''' 
Main function for the Friction Ramp Analysis Software
'''

import sys
from PyQt5.QtWidgets import QApplication
from .classes.definitionClassFrictionRampGUI import (
        frictionRampGUI)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Creates an instance of the vnaReaderMainGui class
    # defined in definition_class_my_vna_reader_main_gui
    # It opens the main GUI of the program
    w = frictionRampGUI()
    w.show()
    sys.exit(app.exec_())