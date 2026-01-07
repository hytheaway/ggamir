# Tooltips

import tkinter as tk

class ToolTip(
    object
):  # https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def show_tooltip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        tooltip_label = tk.Label(
            tw,
            text=self.text,
            justify="left",
            background="#ffffe0",
            foreground="black",
            relief="solid",
            borderwidth=0,
            font="TkDefaultFont 10 normal",
        )
        tooltip_label.pack(ipadx=1)

    def hide_tooltip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def create_tooltip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.show_tooltip(text)
    def leave(event):
        toolTip.hide_tooltip()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

if __name__ == '__main__':
    pass