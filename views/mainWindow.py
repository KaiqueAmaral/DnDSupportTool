from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from views.sideBarMenu import SideBarMenu
from views.homePage import HomePage
from views.contentArea import ContentArea
from typing import Optional
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from pathlib import Path



class MainWindow(QMainWindow):
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QHBoxLayout(self.centralWidget)
        
        self.contentArea = ContentArea()    
        self.sideBarMenu = SideBarMenu()             
        
        self.addWidgetToMainLayout(self.sideBarMenu)     
        self.addWidgetToMainLayout(self.contentArea)
        
        self.sideBarMenu.pageChange.connect(self._switchPageContentArea)
        
        self.setWindowTitle("DnD5e support tool")
        
        
    def addWidgetToMainLayout(self, widget: QWidget):
        self.mainLayout.addWidget(widget)
    
    @Slot(str)
    def _switchPageContentArea(self, pageName: str):
        
        self.contentArea.setCurrentWidget(self.contentArea.pages[pageName])
        