import reflex as rx
from .fonts import Fonts
from .colors import Colors, TextColors
STYLE_SHEETS = [
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "color": TextColors.PRIMARY.value,
    "background": Colors.PRIMARY.value
}