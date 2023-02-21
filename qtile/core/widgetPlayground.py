import os
import colors
import decorations
from core.groups import workspace_names
from libqtile import widget 
from qtile_extras import widget

p1 = decorations.powerline(True, 0, "forward_slash", 0, 17)
p2 = decorations.powerline(False, 1, "forward_slash", 20, 20 )
p3 = decorations.powerline(True, 1, "forward_slash", 5, 18 )
p4 = decorations.powerline(False, 1, "back_slash", 100, 200 )

# WidgetBox for Columns Layout
colBox = widget.WidgetBox(widgets=[
            widget.GroupBox(
                active=colors.st[3],
                visible_groups = workspace_names[0:5],
                hide_unused=False,
                highlight_method="line",
                highlight_color=[colors.op[5], colors.op[11]],
                margin=3,
                inactive=colors.op[4],
                this_current_screen_border=colors.op[14],
                background=colors.op[8],
                fontsize = 16,
                margin_y = 4,
                ),
            widget.GroupBox(
                active=colors.st[3],
                visible_groups = workspace_names[5:9],
                hide_unused=True,
                highlight_method="line",
                highlight_color=[colors.op[5], colors.op[14]],
                margin=3,
                inactive=colors.op[4],
                this_current_screen_border=colors.op[14],
                background=colors.op[8],
                fontsize = 17,
                margin_y = 5,
                ),
                ],
            text_closed = '',
            text_open = '' 
                 )

# WidgetBox for Max Layout
maxBox =  widget.WidgetBox(widgets=[
            widget.GroupBox(
                active=colors.st[1],
                visible_groups = workspace_names[0:5],
                hide_unused=False,
                highlight_method="line",
                highlight_color=[colors.op[5], colors.op[11]],
                margin=3,
                inactive=colors.op[4],
                this_current_screen_border=colors.op[14],
                background=colors.op[8],
                fontsize = 16,
                margin_y = 4,
                ),
            widget.GroupBox(
                active=colors.st[1],
                visible_groups = workspace_names[5:9],
                hide_unused=True,
                highlight_method="line",
                highlight_color=[colors.op[5], colors.op[14]],
                margin=3,
                inactive=colors.op[4],
                this_current_screen_border=colors.op[14],
                background=colors.op[8],
                fontsize = 17,
                margin_y = 5,
                ),
                ],
                text_closed = '',
                text_open = ''
                )

def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            padding=0,
            width=20,
            scale=1,
            **p2
            ),
        colBox,
        maxBox,
        widget.TextBox(
        " ", background = colors.op[8], **p3),
        widget.Prompt(
            **p2
            ),
        widget.Spacer(),
        widget.Chord(
            chords_colors={
                "launch": (colors.op[7], colors.op[9]),
                },
            name_transform=lambda name: name.upper(),
            ),
        widget.Image(
            filename='~/.config/qtile/custom/ender.png'
            ),
        widget.Wttr(
            location={'Malmö': 'Malmö'},
            format='%t %C ' ,
            foreground=colors.op[10],
            background=colors.op[14]
            ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=colors.op[10],
            background=colors.op[14]
            ),
        widget.Volume(
            foreground=colors.op[10],
            scroll_interval=0.03,
            fontsize=14,
            background=colors.op[14]
            ),
        widget.Systray(
            background=colors.op[14]
            ),
        ]
    return widgets_list

Altbox =  widget.GroupBox(
            active=colors.op[7],
            hide_unused=True,
            highlight_method="line",
            highlight_color=[colors.op[8], colors.op[8]],
            margin=3,
            inactive=colors.op[7],
            this_current_screen_border=colors.op[9],
            background=colors.op[8],
            **p1 
            )

