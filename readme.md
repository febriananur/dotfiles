
# Dotfiles Qtile

My Personal Qtile dotfiles



## Installation


```bash
  sudo pacman -S python-pip              #install python pip
  sudo rm /usr/lib/python3.12/EXTERNALLY-MANAGED   #fix error python external managed
  pip install psutil                     #install qtile library
  sudo pacman -S qtile                   #install Qtile WM   
  sudo pacman -S alacritty               #install alacritty terminal  OR
  sudo pacman -S kitty                   #install kitty terminal   
  sudo pacman -S picom                   #install compositor
  sudo pacman -S rofi                    #menu   
  sudo pacman -S lxappearance nitrogen   #install theme manager and wallpaper manager     
  yay -S pa-applet-git                   #install volume icon   
  yay -S betterlockscreen                #install lockscreen

  fc-cache -f -v                         #font refresh
  yay -S sublime-text-4                  #install sublime text editor
                   
```
    
## Pipewire fix audio on VM


sudo cp /usr/share/pipewire/pipewire.conf /etc/pipewire/ 
mkdir -p ~/.config/wireplumber/main.lua.d 
mkdir -p ~/.config/wireplumber/wireplumber.conf.d 
cd ~/.config/wireplumber/wireplumber.conf.d 
cp /usr/share/wireplumber/wireplumber.conf.d/alsa-vm.conf .

Then open ~/.config/wireplumber/wireplumber.conf.d/alsa-vm.conf in an editor and tweak the configuration at the very bottom of the file to suit the needs. Like:

```

      ["api.alsa.period-size"]   = 1024

      ["api.alsa.headroom"]      = 8192
```
