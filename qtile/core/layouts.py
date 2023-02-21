from libqtile import layout
from libqtile import qtile
from libqtile.config import Match
from libqtile.layout import floating
import colors


layout_theme =  {"border_width": 1,
            "margin": 3,
            "border_focus": colors.ex["extra7"],
            "border_normal": colors.ex["darkgray"],
            "border_on_single": True
    }    

layout_no_border =  {"border_width": 1,
            "margin": 0,
            "border_focus": colors.ex["extra7"],
            "border_normal": colors.ex["darkgray"],
            "border_on_single": True
    }    

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    #     layout.Stack(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme)
]
def get_layout_index():
     names = [
              "columns",
              "max",
              "floating"
              #"monadwide",
              #"ratiotile",
              #"stack",
              #"treetab"
             ]
     return names.index(qtile.current_layout.name) + 1

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
        border_focus = colors.st["frthStr"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
wmname = "LG3D"
