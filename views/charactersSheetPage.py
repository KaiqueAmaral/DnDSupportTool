from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from typing import Optional
from views.constants import SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME


class CharactersSheetPage(QWidget):
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setObjectName(SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME)
        self.layout = QHBoxLayout(self)
        
        self.layout.addWidget(QLabel("<h1>Character sheet Page</h1>"))