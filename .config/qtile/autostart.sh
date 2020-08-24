#! /bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}
#run wal --theme base16-black-metal-immortal 
run feh --bg-fill /home/al/Pictures/noisewp.png  &
run picom --config $HOME/.config/picom/picom.conf &
#run nitrogen --restore &
run urxvtd -q -o -f &
#run variety &
run nm-applet &
#run pamac-tray &
run xfce4-power-manager &
run xautolock -corners 000- -time 10 -locker blurlock &
