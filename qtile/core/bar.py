from libqtile import bar
from qtile_extras import widget
from core.widgets import *
import colors

widget_defaults = dict(
    #font="JetBrainsMono Nerd Font Medium",
    font="DejaVu Sans Book",
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()

widgets = init_widgets_list()



def create_bar(s):
    if s == 0:
        return bar.Bar(
            widgets,
            size = 25,
            margin=[2, 6, 2, 6],
            border_width=[0, 0, 0, 0],
            border_color= colors.st["mainWeak"],
            background=colors.st["mainStr"],
            opacity= 1
        )

main_screen_bar = create_bar(0)
