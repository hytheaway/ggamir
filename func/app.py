# Application handling

import sys
import pygame
import gui.lookandfeel

def rootManagement(root):
    root.iconphoto(False, gui.lookandfeel.icon_photo)
    if sys.platform == 'win32':
        gui.lookandfeel.apply_theme_to_titlebar(root)
    root.focus_force()
    root.title("GGAMIR")
    root.protocol('WM_DELETE_WINDOW', lambda: sys.exit())

def quit_function():
    """
    Quit function that properly closes out of pygame and the python script, which prevents a segfault when this project is compiled by nuitka.
    """    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    pass