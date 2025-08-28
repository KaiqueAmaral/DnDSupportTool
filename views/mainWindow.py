from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from views.sideBarMenu import SideBarMenu
from typing import Optional



class MainWindow(QMainWindow):
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout(self.centralWidget)
        
        
        
        
        self.sideBarMenu = SideBarMenu()
        self.addWidgetToMainLayout(self.sideBarMenu)
        
        self.content_area = QWidget()
        self.mainLayout.addWidget(self.content_area)
        
        self.setWindowTitle("DnD5e support tool")
        
        
    def addWidgetToMainLayout(self, widget: QWidget):
        self.mainLayout.addWidget(widget)