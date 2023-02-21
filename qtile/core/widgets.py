import os
import colors
import decorations
from libqtile import qtile
from core.groups import workspace_names
from libqtile import widget
from qtile_extras import widget

p1 = decorations.powerline(True, 0, "forward_slash", 0, 17)
p2 = decorations.powerline(False, 1, "forward_slash", 20, 20)
p3 = decorations.powerline(True, 1, "forward_slash", 0, 16) 
# p3 = decorations.powerline(True, 0, "back_slash", 0, 0)
# p4 = decorations.powerline(True, 0, "rounded_right", 0, 7)


sysTray = widget.WidgetBox(widgets=[
    widget.Systray(
        background=colors.st["mainWeak"],
    ),
],
    background=colors.st["mainWeak"],
    fontsize=13,
    foreground=colors.st["focExt"],
    text_closed=' ',
    text_open=' ',
)

weather = widget.WidgetBox(widgets=[
    widget.Wttr(
        location={'Malmö': 'Malmö'},
        format='%t %C ',
        foreground=colors.st["focExt"],
        background=colors.st["mainWeak"]
    ),
],
    background=colors.st["mainWeak"],
    fontsize=18,
    foreground=colors.st["focExt"],
    text_closed='  ',
    text_open='  ',
)


def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=0,
            width=20,
            scale=1,
            **p2
        ),
        widget.GroupBox(
            active=colors.st["outExt"],
            visible_groups=workspace_names[0:5],
            hide_unused=False,
            highlight_method="line",
            highlight_color=[colors.st["mainExt"], colors.st["mainExt"]],
            margin=3,
            inactive=colors.ex["extra8"],
            this_current_screen_border=colors.ex["extra7"],
            background=colors.st["mainExt"],
            fontsize=16,
            margin_y=4,
        ),
        widget.GroupBox(
            active=colors.st["outExt"],
            visible_groups=workspace_names[5:9],
            hide_unused=True,
            highlight_method="line",
            highlight_color=[colors.st["mainExt"], colors.st["mainExt"]],
            margin=3,
            inactive=colors.ex["extra8"],
            this_current_screen_border=colors.ex["extra7"],
            background=colors.st["mainExt"],
            fontsize=17,
            margin_y=5,
            **p3
        ),
        widget.Prompt(
            **p2
        ),
        widget.Spacer(),
        widget.Chord(
            chords_colors={
                "launch": (colors.st["outExt"], colors.ex["white"]),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Image(
            filename='~/.config/qtile/icons/ender.png'
        ),
        weather,
        widget.Volume(
            theme_path='/home/ozz/.config/qtile/icons/volume/',
            foreground=colors.st["focExt"],
            scroll_interval=1.5,
            fontsize=10,
            background=colors.st["mainWeak"],
            padding=5
        ),
        widget.BatteryIcon(
            background=colors.st["mainWeak"],
            theme_path='/home/ozz/.config/qtile/icons/battery/',
            battery=1,
            margin_x=5
        ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=colors.st["focExt"],
            background=colors.st["mainWeak"],
            mouse_callbacks={'Button1': qtile.spawn(
                "alacritty -e 'bash -c \"cal; read\"'")}
        ),
        sysTray,
        widget.Spacer(
            length=5,
            background=colors.st["mainWeak"]
        ),
    ]
    return widgets_list
