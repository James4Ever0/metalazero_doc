target=$(ps wwwaux | grep auth | grep xvfb | grep -Eo "/tmp.\$")
export XAUTHORITY=$target && export DISPLAY=:99 && xdotool mousemove 500 500
# this can only be done without vncserver.
