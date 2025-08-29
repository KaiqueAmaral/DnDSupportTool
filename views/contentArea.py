from PySide6.QtWidgets import QStackedWidget
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget

class ContentArea(QStackedWidget):
    def __init__(self, parent: Optional ['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)