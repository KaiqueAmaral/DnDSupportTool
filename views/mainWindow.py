from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from views.sideBarMenu import SideBarMenu
from views.homePage import HomePage
from views.contentArea import ContentArea
from typing import Optional



class MainWindow(QMainWindow):
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout(self.centralWidget)
        
        self.contentArea = ContentArea()    
        self.sideBarMenu = SideBarMenu(self.contentArea)
                
        self.addWidgetToMainLayout(self.sideBarMenu)     
        self.addWidgetToMainLayout(self.contentArea)
        
        self._configPages()
        
        self.setWindowTitle("DnD5e support tool")
        
        
    def addWidgetToMainLayout(self, widget: QWidget):
        self.mainLayout.addWidget(widget)
        
    def _configPages(self):
        self.pages = {
            "home": HomePage()
        }