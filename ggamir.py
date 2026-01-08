# Garrett's Great Analyzer of Mono IRs

# Global variables to be shared across all files that need it.
import shared.globals

# Start up (must be before GUI imports)
import gui.startup

if __name__ == '__main__':
    shared.globals.root = gui.startup.start_up()

import gui.windowmanagement
import gui.initcontent
import func.app

if __name__ == '__main__':
    gui.windowmanagement.centered_window(shared.globals.root)
    gui.initcontent.populate_root(shared.globals.root)
    func.app.root_management(shared.globals.root)
    
    shared.globals.root.mainloop()