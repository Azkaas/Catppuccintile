from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

def powerline(boolx, rad, slash, shi, sz):
    line = {
        "decorations": [
            RectDecoration(use_widget_background = boolx, padding_y = 0, filled = True, radius = rad),
            PowerLineDecoration(path = slash, padding_y = 0, shift = shi, size = sz)
        ]
    }
    return line
