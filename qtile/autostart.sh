#!/bin/bash

function run {
	if ! pgrep $1 ;
	then 
		$@&
	fi
}


# systray battery icon
# cbatticon -u 5 &

# run nitrogen --restore  &
#run picom &
#picom --backend glx -b
run nm-applet &
run pa-applet &
run nitrogen --restore  &
# run conky -c Downloads/conky/gotham &

# systray volume
volumeicon & 
