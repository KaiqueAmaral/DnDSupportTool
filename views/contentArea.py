from PySide6.QtWidgets import QStackedWidget
from typing import Optional, TYPE_CHECKING
from views.homePage import HomePage
from views.charactersSheetPage import CharactersSheetPage
from views.constants import SIDE_BAR_HOME_BUTTON_NAME, SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget

class ContentArea(QStackedWidget):
    def __init__(self, parent: Optional ['QWidget'] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.pages = {
            SIDE_BAR_HOME_BUTTON_NAME: HomePage(), 
            SIDE_BAR_CHARACTER_SHEET_BUTTON_NAME: CharactersSheetPage()
        }
        
        for page in self.pages.values():
            self.addWidget(page)
        
        