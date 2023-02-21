from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from core.keys import keys, mod, shift
from core.settings import workspace_names

workspaces = [
    {"name": workspace_names[0], "key": "1",      "matches": [Match(wm_class="firefox")], "lay": "columns"},
    {"name": workspace_names[1], "key": "2",      "matches": [Match(wm_class="neovim")], "lay": "columns"},
    {"name": workspace_names[2], "key": "3",      "matches": [Match(wm_class="Thunar")], "lay": "columns"},
    {"name": workspace_names[3], "key": "4",      "matches": [Match(wm_class="Gimp"), Match(wm_class="mpv"), Match(wm_class="Kodi"), Match(wm_class="youtube")], "lay": "columns"},
    {"name": workspace_names[4], "key": "5",      "matches": [Match(wm_class="bpytop")], "lay": "columns"},
    {"name": workspace_names[5], "key": "6",      "matches": [], "lay": "columns"},
    {"name": workspace_names[6], "key": "7",      "matches": [Match(wm_class="cypress")], "lay": "columns"},
    {"name": workspace_names[7], "key": "8",      "matches": [Match(wm_class="cypress")], "lay": "columns"},
    {"name": workspace_names[8], "key": "9",      "matches": [Match(wm_class="cypress")], "lay": "columns"},
    
]

groups = [Group(i) for i in "123456789"]
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=False),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            workspace["key"],
            *(
                lazy.window.togroup(workspace["name"]),
                #lazy.group[workspace["name"]].toscreen(toggle=False),
            ),
            desc="Move focused window to another group",
        )
    )

del groups[:9]
# Append scratchpads to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('nnn', 'alacritty -e nnn -d -C', height=0.8, width=0.7, x=0.15, y=0.1),
    DropDown('terminal', 'alacritty', height=0.8, width=0.7, x=0.15, y=0.1),
 ]))
   
keys.extend([
    Key(["mod1"], "1", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key(["mod1"], "2", lazy.group['scratchpad'].dropdown_toggle('nnn')),
])
