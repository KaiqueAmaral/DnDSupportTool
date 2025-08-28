from PySide6.QtWidgets import QPushButton
from typing import Optional

class SideBarButton(QPushButton):
    def __init__(self, name, parent: Optional['QWidget'] = None, *args, **kwargs):
        super().__init__(name, parent, *args, **kwargs)
        
        
        
        