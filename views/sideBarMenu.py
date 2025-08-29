from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from views.sideBarButton import SideBarButton
from views.contentArea import ContentArea
from views.constants import SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME, SIDE_BAR_HOME_BUTTON_NAME, SIDE_BAR_RULES_BUTTON_NAME
from PySide6.QtCore import Slot
from typing import Optional


class SideBarMenu(QWidget):
    
    def __init__(self, contentArea: 'ContentArea', parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.verticalLayout = QVBoxLayout(self)
        
        self._createMenuButtons()
        self._createButtonsSlots()
        
        self._addButtonsToLayout()
               
        self.verticalLayout.addStretch()
    
    
    def _createMenuButtons(self):
        self.buttons =  (
            SideBarButton(SIDE_BAR_HOME_BUTTON_NAME), 
            SideBarButton(SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME), 
            SideBarButton(SIDE_BAR_RULES_BUTTON_NAME)
        )
        
    def _addButtonsToLayout(self):
        for button in self.buttons:
            self.verticalLayout.addWidget(button)
    
    
    def _createButtonsSlots(self):
        for button in self.buttons:
            buttonText = button.text()
            
            buttonSlot = self._createSlot(
                self._switchPageFromContentArea,
                buttonText
                )
            
            self._connectButtonClicked(button, buttonSlot)
            
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _createSlot(self, function, *args, **kwargs):
        @Slot()
        def realSlot():
            function(*args, **kwargs)
        return realSlot
    
    def _switchPageFromContentArea(self, buttonText):
        print(buttonText)
        
        
               
        
        
        
        
    
    