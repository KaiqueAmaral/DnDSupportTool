import sys
from PySide6.QtWidgets import QApplication
from views.mainWindow import MainWindow
from views.sideBarMenu import SideBarMenu 

if __name__ == '__main__':
    
    app = QApplication(sys.argv)  
    window  = MainWindow()
    
    
    window.show()

    sys.exit(app.exec())
