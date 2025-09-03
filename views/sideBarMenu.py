from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from views.sideBarButton import SideBarButton
from views.constants import SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME, SIDE_BAR_HOME_BUTTON_NAME, SIDE_BAR_RULES_BUTTON_NAME
from PySide6.QtCore import Signal, Slot
from typing import Optional


class SideBarMenu(QWidget):
    pageChange = Signal(str)

    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.verticalLayout = QVBoxLayout(self)
        
        # TODO: Passar valores hardcoded para variáveis
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        
        self._createMenuButtons()
        self._createMenuButtonsSlots()
        
        self._addButtonsToLayout()
               
        self.verticalLayout.addStretch()
    
    
    
    def _createMenuButtons(self) -> None:
        self.buttons =  (
            SideBarButton(SIDE_BAR_HOME_BUTTON_NAME), 
            SideBarButton(SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME), 
            SideBarButton(SIDE_BAR_RULES_BUTTON_NAME)
        )
    
    
    def _addButtonsToLayout(self) -> None:
        for button in self.buttons:
            self.verticalLayout.addWidget(button)
    
    
    
    def _createMenuButtonsSlots(self) -> None:
        for button in self.buttons:
            buttonText = button.text()
            
            slot = self._createSlot(
                self._emitSignal,
                buttonText
            )
            
            self._connectButtonClicked(button, slot)
    
        
    def _connectButtonClicked(self, button: SideBarButton, slot: Slot):
        button.clicked.connect(slot)
        
    
    def _createSlot(self, function, *args, **kwargs):
        @Slot()
        def realSlot():
            function(*args, **kwargs)
        return realSlot
    
    def _emitSignal(self, buttonText: str) -> None:
        self.pageChange.emit(buttonText)
        
        
        
        
               
        
        
        
        
    
    