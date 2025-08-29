from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from typing import Optional


class HomePage(QWidget):
    def __init__(self, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(QLabel("<h1>Ficha de Personagem</h1>"))
        
        