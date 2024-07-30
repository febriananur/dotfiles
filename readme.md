Do This First :


1│ sudo pacman -S python-pip <br>
2  │ sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED <br>
3  │ pip install psutil <br>
4  │ sudo pacman -S qtile <br>
5  │ sudo pacman -S alacritty <br>
6  │ pip install pulsectl-asyncio <br>
7  │ sudo pacman -S rofi <br>
8  │ pulseaudio --start <br>
9  │ systemctl --user pulseaudio <br>
10 │ sudo pacman -S lxappearance nitrogen <br>
11 │ yay -S sublime-text-4 <br>
12 │ sudo pacman -S picom <br>
13 │ yay -S betterlockscreen <br>
14 │ fc-cache -f -v <br>
15 │ sudo pacman -S pulseaudio <br>
16 │ sudo pacman -S nitrogen <br>
17 | yay -S pa-applet-git


pipewire config

sudo cp /usr/share/pipewire/pipewire.conf /etc/pipewire/
mkdir -p ~/.config/wireplumber/main.lua.d
mkdir -p ~/.config/wireplumber/wireplumber.conf.d
cd ~/.config/wireplumber/wireplumber.conf.d
cp /usr/share/wireplumber/wireplumber.conf.d/alsa-vm.conf 

Then open `~/.config/wireplumber/wireplumber.conf.d/alsa-vm.conf` in an editor and tweak the configuration at the very bottom of the file to suit the needs. Like:



```

      ["api.alsa.period-size"]   = 1024

      ["api.alsa.headroom"]      = 8192

```

