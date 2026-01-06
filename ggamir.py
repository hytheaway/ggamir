# Garrett's Great Analyzer of Mono IRs

# OS
import sys
import os
import tempfile

# Math
import numpy as np
import matplotlib.pyplot as plt

# Start up (must come before GUI imports)
import gui.startup

if __name__ == '__main__':
    root = gui.startup.startUp()

# GUI
import gui.lookandfeel
import gui.windowmanagement
import gui.content

# Functions
import func.app

if __name__ == '__main__':
    gui.windowmanagement.centered_window(root)
    
    gui.content.populateRoot(root)
    
    func.app.rootManagement(root)
    root.mainloop()