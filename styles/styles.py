from views.constants import (SIDE_BAR_BUTTONS_BACKGROUND_COLOR, 
SIDE_BAR_BUTTONS_TEXT_COLOR, 
SIDE_BAR_BUTTONS_HOOVER_BACKGROUND_COLOR,
BIG_FONT_SIZE,
MEDIUM_FONT_SIZE,
SMALL_FONT_SIZE
)

QSS = f"""
QMainWindow, QWidget {{
    background-color: #5c5c5c;
    color: #e0e0e0;
}}


SideBarButton {{
    background-color: {SIDE_BAR_BUTTONS_BACKGROUND_COLOR};
    color: {SIDE_BAR_BUTTONS_TEXT_COLOR};
    border: 1px solid #0c0c0c;
    padding: 10px;
    font-size: {MEDIUM_FONT_SIZE};
    text-align: left;
}}

SideBarButton:hover {{
    background-color: {SIDE_BAR_BUTTONS_HOOVER_BACKGROUND_COLOR};
}}
"""


def setupTheme(app): 
    # Sobrepor com o QSS personalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + QSS)

