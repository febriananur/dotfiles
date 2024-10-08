from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=0)

def separatorl(fg="light", bg="dark"):
    return widget.Sep(**base(fg, bg), linewidth=0, padding=15)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3,
        margin=0,
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text=" ", # Icon: nf-oct-triangle_left
        fontsize=120,
        padding=-45,
    )


def powerlineright(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=30,
        padding=0
    )
    

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light',bg='dark5'),
            font='JetBrainsMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['color1'],
            inactive=colors['color4'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['dark1'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
         powerlineright('dark5', 'dark'),

        separator(),
        icon(bg="dark",fg="color5", fontsize=17, text=''),
        widget.WindowName(**base(fg='grey'), fontsize=14, padding=5,font='JetBrainsMono Nerd Font semibold',),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('dark', 'dark'),
    # icon(bg="dark",fg="color7", fontsize=17, text=''),
    icon(bg="dark",fg="color3", fontsize=17, text='  '),
    widget.CPU(**base(bg='dark',fg='grey'),format='{load_percent}%'),

    icon(bg="dark",fg="color4", fontsize=17, text='  '),
    widget.DF(
        **base(bg='dark',fg='grey'),
        visible_on_warn=False,
        format='{uf}{m}'),

    icon(bg="dark",fg="color5", fontsize=17, text='  '),
    widget.Memory(
        **base(bg='dark',fg='grey'),
        format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}'),
        icon(bg="dark",fg="color7", fontsize=17, text=''),

    separatorl('dark2', 'dark'),

    powerline('dark2', 'dark'),

    icon(bg="dark2",fg="color7", text='󰀂 '),  # Icon: nf-fa-feed
    
    # widget.Net(**base(bg='dark2',fg='color7'), interface='enp0s3',format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}'),
    widget.NetGraph(border_color='3b4261', background='3b4261',graph_color='a6e3a1',fill_color='65b35f'),

    # widget.Net(border_color='4C566A', background='4C566A',graph_color='a6e3a1',foreground='a6e3a1', interface='enp0s3'),   
    separatorl('dark3', 'dark2'),

    powerline('dark3', 'dark2'),

    widget.CurrentLayoutIcon(**base(bg='dark3'),custom_icon_paths=["/home/fx/.config/qtile/layout-icons/gruvbox-light2"], scale=0.45),

    widget.CurrentLayout(**base(bg='dark3',fg='color3'), padding=5),    


    separatorl('color2', 'dark3'),

    powerline('dark4', 'dark3'),

    icon(bg="dark4",fg="color4", fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='dark4',fg='color4'), format='%d/%m/%Y - %H:%M '),

    
    # separatorl('dark4', 'dark4'),

#     powerline('dark5', 'dark4'),

#     icon(bg="dark5",fg='color5', text=' '),
    
#     # widget.Volume(**base(bg='color1')),

# # must install "pip install pulsectl-asyncio for code below"
#     widget.PulseVolume(
#         **base(bg='dark5',fg='color5'),
#         check_mute_string=['on'],
#         ),

    # separatorl('color6', 'dark4'),

    powerline('color6', 'dark4'),


    widget.Systray(background=colors['color6'], padding=10),


    # separatorl('color6', 'color6'),


    # icon(fg="light",bg="color6", text='  '), # Icon: nf-fa-download
    
    # widget.CheckUpdates(
    #     **base(bg='color6'),
    #     colour_have_updates=colors['light'],
    #     colour_no_updates=colors['light'],
    #     no_update_string='0',
    #     display_format='{updates}',
    #     update_interval=1800,
    #     custom_command='checkupdates',
    #     distro='Ubuntu'
    # ),

    separatorl('color6', 'color6'),



]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),

    # widget.Clock(**base(bg='color1')),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
