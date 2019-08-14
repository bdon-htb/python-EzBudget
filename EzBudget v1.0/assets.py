import cfg, os

#Get directories of images.
img_exit_button_off = os.path.join(cfg.ui_dir,'exit_off.png')
img_exit_button_on = os.path.join(cfg.ui_dir,'exit_on.png')
img_logo = os.path.join(cfg.ui_dir,'logo.png')
img_waffle = os.path.join(cfg.ui_dir,'waffle_small.png')
img_edit_data = os.path.join(cfg.ui_dir,'edit_data.png')
img_graphs = os.path.join(cfg.ui_dir,'graphs.png')
img_stats = os.path.join(cfg.ui_dir,'stats.png')
img_icon = os.path.join(cfg.ui_dir,'icon.ico')
img_menu_button = os.path.join(cfg.ui_dir, 'button_list.png')
img_menu_menus = os.path.join(cfg.ui_dir, 'menu_list.png')
img_menu_tips = os.path.join(cfg.ui_dir, 'steps_list.png')

#Get directories of fonts.
font_roboto_light = os.path.join(cfg.font_dir, 'Roboto-Light.ttf')

#Set colours based on their hexadecimal values.
colours = {
    'silver':'#f2f2f2',
    'darken':'#1d1d1d',
    'lightgreen':'#b8eda2',
    'green':'#0fc141',
    'darkgreen':'#1e7145',
    'background': '#ee1111', #This is just red. Simply used for testing purposes.
        }

#Set the fonts of the application.
fonts = {
    'title':font_roboto_light
}

#Set ui elements of the main window.
ui = {
	'exit_button': [img_exit_button_on,img_exit_button_off],
	'logo': img_logo,
	'waffle': img_waffle,
	'edit_data':img_edit_data,
	'graphs':img_graphs,
	'stats':img_stats,
	'icon':img_icon,
}

#Set the images of the help menu.
help_menu = {
	'buttons':img_menu_button,
	'menus':img_menu_menus,
	'steps':img_menu_tips
}
