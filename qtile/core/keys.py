from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h",  lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    Key([mod, "shift"], "Return",lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(["control", "mod1"], "delete", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5 -u"), desc="Decrease Volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5 -u"), desc="Increase Volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle &&"), desc="Toggle Mute"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle play"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous"),
    # Backlight
    Key([], "XF86MonBrightnessUp", lazy.spawn("brillo -u 200000 -A 10; notify-send 'brightness up'"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brillo -u 200000 -U 10; notify-send 'brightness down'"), desc="Brightness up"),
    # Custom keybinds
    Key([mod], "F2", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "t", lazy.spawn("alacritty --class neovim -e nvim"), desc="Launch Neovim"),
    Key([mod], "o", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Launch emacs"),
    Key([mod], "b", lazy.spawn("alacritty --class bpytop -e bpytop"), desc="Launch Bpytop"),
    Key([mod], "m", lazy.spawn("alacritty --class youtube  yt"), desc="Launch yt"),

    Key([mod], "d", lazy.spawn("dmenu_run -h 25 -x 80 -y 2 -z 1834 -fn 'DejaVu Sans Book 5:pixelsize=14' -nb '#11111b' -nf '#cdd6f4' -sb '#cdd6f4' -sf '#11111b'"), desc="Launch dmenu"),
    Key(["mod1"], "d", lazy.spawn("via -r"), desc="Launch via"),
    Key([mod], "e", lazy.spawn("Thunar"), desc="Launch Thunar"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    # Flameshot
    Key([], "Print", lazy.spawn("flameshot screen"), desc="Screenshot"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Flameshot clip"),
    #Key([mod], "section", lazy.function(switch_monitor), desc="Switch focused monitor"),
    Key([mod], "section", lazy.next_screen(), desc="Change monitor focus"),
    # Key([mod], "i", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    #Dmenu
    Key([mod], "p", lazy.spawn("/home/ozz/scripts/confedit"), desc="Edit files Dmenu"),
]
# def show_keys():
#     key_help = ""
#     for i in range(0, len(keys)):
#         k = keys[i]
#         if not isinstance(k, Key):
#             continue
#         mods = ""
#
#         for m in k.modifiers:
#             if m == "mod4":
#                 mods += "Super + "
#             else:
#                 mods += m.capitalize() + " + "
#
#         if len(k.key) > 1:
#             mods += k.key.capitalize()
#         else:
#             mods += k.key
#
#         key_help += "{:<25} {}".format(mods, k.desc + ("\n" if i != len(keys) - 1 else ""))
#
#     return key_help
#
# keys.extend(
#     [
#         Key(
#             [mod],
#             "a",
#             lazy.spawn(
#                 "sh -c 'echo \""
#                 + show_keys()
#                 + '" | rofi -dmenu -theme ~/.config/rofi/hotkeys.rasi -i -p ""\''
#             ),
#             desc="Print keyboard bindings",
#         ),
#     ]
# )
