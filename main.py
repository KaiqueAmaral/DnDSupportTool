import sys
from PySide6.QtWidgets import QApplication
from views.mainWindow import MainWindow
from styles.styles import setupTheme

if __name__ == '__main__':
    app = QApplication(sys.argv)  
   
    setupTheme(app)
    
    window  = MainWindow()
      
    window.show()

    sys.exit(app.exec())
