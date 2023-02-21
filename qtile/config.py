import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.layout.floating import Floating
from libqtile.config import Click, Drag, DropDown, Group, Key, KeyChord, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration
from core import bar as b
from core import widgets, settings, decorations
import colors
from core import widgets as w
from core import layouts as l
from core import keys as k
from core import groups as g
from core.settings import workspace_names


mod = "mod4"
terminal = guess_terminal()
home = os.path.expanduser('~')

if qtile.core.name == "x11":
    term = "urxvt"
elif qtile.core.name == "wayland":
    term = "foo:"

keys = k.keys

groups = g.groups
workspaces = g.workspaces

layout_theme = l.layout_theme

layout_no_border = l.layout_no_border

layouts = l.layouts


widget_defaults = dict(
    # font="JetBrainsMono Nerd Font Medium",
    font="DejaVu Sans Book",
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()


APPLICATION_NAME_SUB = {
    "Firefox": "Firefox",
    "NVIM": "Nvim",
    "Visual Studio Code": "VScode",
    "None": "",
}


def replace_window_title(text):
    for key in APPLICATION_NAME_SUB.keys():
        if key in text:
            return APPLICATION_NAME_SUB[key]
    return text


testbar = b.main_screen_bar
screens = [
    Screen(
        top=testbar,
        bottom=bar.Gap(2),
        left=bar.Gap(4),
        right=bar.Gap(4),
    ),
    Screen(
        top=testbar,
        bottom=bar.Gap(0),
        left=bar.Gap(0),
        right=bar.Gap(0),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
floating_layout = l.floating_layout
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.client_new
def modify_window(client):
    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[group.name]  # there
            targetgroup.toscreen(toggle=False)
            break
            
# @hook.subscribe.client_new
# def disable_floating(window):
#     rules = [
#         Match(wm_class="mpv")
#     ]
#
#     if any(window.match(rule) for rule in rules):
#         window.togroup(qtile.current_group.name)
#         window.cmd_disable_floating()           
# @hook.subscribe.client_new
# def client_new(client):
#
#     if client.get_wm_class() == 'neovim':
#         client.togroup('', switch_group=True)


wmname = "LG3D"
