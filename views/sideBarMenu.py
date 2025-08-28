from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from views.sideBarButton import SideBarButton
from typing import Optional


class SideBarMenu(QWidget):
    
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.verticalLayout = QVBoxLayout(self)
        
        self.homeButton = SideBarButton("Home")
        self.characterSheet = SideBarButton("Character Sheet")
        self.Rules = SideBarButton("Rules")
        
        self.verticalLayout.addWidget(self.homeButton)
        self.verticalLayout.addWidget(self.characterSheet)
        self.verticalLayout.addWidget(self.Rules)
        
        self.verticalLayout.addStretch()
               
        
        
        
        
    
    