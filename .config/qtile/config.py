# -*- coding: utf-8 -*-


##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"                             # My terminal of choice
myConfig = "/home/al/.config/qtile/config.py"    # The Qtile config file location
home = os.path.expanduser('~')


##### KEYBINDINGS #####
keys = [
    # The essentials
    Key(
        [mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal With Fish Shell'
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn(
            "rofi -show drun"),
        desc='rofi Run Launcher'
    ),
    Key(
        [mod, "mod1"], "Return",
        lazy.spawn(
            "rofi -show window"),
        desc='rofi window switcher'
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod, "shift"], "c",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key(
        [mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),
  
    # Window controls
    Key(
        [mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key(
        [mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),
    Key(
        [mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key(
        [mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key(
        [mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
    ),
    # Stack controls
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key(
        [mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),

    # My applications launched with SUPER + ALT + KEY
    Key(
        [mod, "mod1"], "b",
        lazy.spawn("firefox"),
        desc='firefox'
    ),

    Key(
        [mod, "mod1"], "f",
        lazy.spawn(myTerm + " -e ranger"),
        desc='ranger'
    ),
    Key(
        [mod, "mod1"], "m",
        lazy.spawn(myTerm + " -e mocp"),
        desc='Mocp'
    ),
    Key(
        [mod, "mod1"], "e",
        lazy.spawn('emacs'),
        desc='Emacs'
    ),
    Key(
        [mod, "mod1"], "o",
        lazy.spawn('loffice'),
        desc='LibreOffice'
    ),
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key(["mod1"], "h", lazy.spawn('kitty -e htop')),

    Key([], "Print", lazy.spawn(
        "scrot -q 90 'npnx-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
]

##### GROUPS #####
group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 9,
                "border_focus": "#3679D8",
                "border_normal": "#05295A"
                }

##### THE LAYOUTS #####
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme)
]

##### COLORS #####

colors = [["#0D0E16", "#0D0E16"],  #BG 0
          ["#CEDBE5", "#CEDBE5"],  #FG 1
          ["#D83441", "#D83441"],  #RED 2
          ["#79D836", "#79D836"],  #GREEN 3
          ["#D8B941", "#D8B941"],  #YELLOW 4
          ["#3679D8", "#3679D8"],  #BLUE 5
          ["#8041D8", "#8041D8"],  #MAGENTA 6
          ["#36D8BD", "#36D8BD"],  #CYAN 7
          ["#D85F00", "#D85F00"],  #ORANGE 8
          ["#2D9674", "#2D9574"],  #TEAL 9
          ["#AB11D8", "#AB11D8"]]  #VIOLET 10 

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Roboto",
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####
def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.GroupBox(
            font="Roboto",
            fontsize=12,
            margin_y=2,
            margin_x=0,
            padding_y=2,
            padding_x=5,
            borderwidth=2,
            active=colors[4],
            inactive=colors[2],
            rounded=False,
            hide_unused=True,
            highlight_color=colors[0],
            highlight_method="line",
            this_current_screen_border=colors[8],
            this_screen_border=colors[0],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            background=colors[0]
        ),
        widget.WindowName(
            foreground=colors[3],
            background=colors[0],
            padding=0,
            fontsize=11
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.CPU(
            format="CPU {load_percent}%",
            foreground=colors[5],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.TextBox(
            text="🌡",
            padding=2,
            foreground=colors[8],
            background=colors[0],
            fontsize=11
        ),
        widget.ThermalSensor(
            foreground=colors[8],
            background=colors[0],
            padding=5
        ), widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.TextBox(
            text="⟳",
            padding=0,
            foreground=colors[6],
            background=colors[0],
            fontsize=11
        ),
        widget.Pacman(
            execute="kitty sudo pacman -Syu",
            update_interval=180,
            foreground=colors[6],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.TextBox(
            text="🖬",
            foreground=colors[9],
            background=colors[0],
            padding=0,
            fontsize=12
        ),
        widget.Memory(
            foreground=colors[9],
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.TextBox(
            text="📢",
            foreground=colors[1],
            background=colors[0],
            padding=0
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.Volume(
            foreground=colors[1],
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.TextBox(
            text="🔋", 
            foreground=colors[4],
            background=colors[0],
            padding=0
        ),
        widget.Battery(
            foreground=colors[4],
            background=colors[0],
            low_percentage = 0.2,
            padding=5,
            format="{char} {percent:2.0%}"
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            background=colors[0]
        ),
        widget.Clock(
            foreground=colors[7],
            background=colors[0],
            format="%B %d  %H:%M "
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=colors[0]
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=colors[0]
        ),
    ]
    return widgets_list

# # ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# # BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["WWW"] = ["Qutebrowser", "Firefox", "Navigator", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#                 "qutebrowser", "firefox", "naviagtor", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["DEV"] = ["Atom", "Emacs", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                 "atom", "emacs", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["GIMP"] = ["Gimp", "gimp"]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld"]
#     d["MEDIA"] = ["Vlc", "vlc", "Mpv", "mpv", "mocp"]
#     d["OFFICE"] = ["libreoffice"]
#     d["FIlES"] = ["Thunar", "Nemo", "Ranger", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#                   "thunar", "nemo", "ranger", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird"]

#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]

#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# # END
# # ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME

# Screens #


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=22)), ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
