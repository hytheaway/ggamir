# Alert windows, including error and message windows

import shared.globals

import gui.lookandfeel
import gui.windowmanagement
import gui.tooltips


def error_window(
    root = shared.globals.root,
    icon_photo = gui.lookandfeel.icon_photo,
    error_message: str = "Generic Error Message",
    title: str = "Error",
    width: int = 300,
    height: int = 120,
    **kwargs,
):
    """
    Creates an error window.

    Args:
        error_message (str, optional): Error message to be displayed. Defaults to 'Generic Error Message'.
        title (str, optional): Title of window. Defaults to 'Error'.
        width (int, optional): Width of window. Defaults to 300.
        height (int, optional): Height of window. Defaults to 120.

    Keyword Arguments:
        tooltip_text (str, optional): If a string is provided, a tooltip will appear with that string when hovering over the error message.

    Returns:

    """
    tooltip_text = kwargs.get("tooltip_text", None)
    errorWindow = gui.lookandfeel.tk.Toplevel(root)
    errorWindow.iconphoto(False, icon_photo)
    gui.windowmanagement.centered_window(errorWindow)
    errorWindow.title(str(title))
    errorWindow.geometry(str(width) + "x" + str(height))
    errorWindow.minsize(width, height)
    errorMessageLabel = gui.lookandfeel.ttk.Label(
        errorWindow, text="\nError: " + str(error_message) + "\n", justify="center"
    )
    if tooltip_text:
        gui.tooltips.create_tooltip(errorMessageLabel, text=str(tooltip_text))
    errorMessageLabel.pack()
    errorConfirmButton = gui.lookandfeel.ttk.Button(
        errorWindow,
        text="OK",
        style="my.TButton",
        command=lambda: errorWindow.destroy(),
    )
    errorConfirmButton.pack()
    errorWindow.focus_force()
    gui.lookandfeel.apply_theme_to_titlebar(errorWindow)
    return -1

def message_window(
    root = shared.globals.root,
    icon_photo = gui.lookandfeel.icon_photo,
    message: str = "Generic Message",
    title: str = "Title",
    width: int = 300,
    height: int = 120,
    **kwargs,
):
    """
    Creates a message/alert window.

    Args:
        message (str, optional): Message to be displayed. Defaults to 'Generic Message'.
        title (str, optional): Title of window. Defaults to 'Title'.
        width (int, optional): Width of window. Defaults to 300.
        height (int, optional): Height of window. Defaults to 120.

    Keyword Arguments:
        tooltip_text (str, optional): If a string is provided, a tooltip will appear with that string when hovering over the message.

    Returns:

    """
    tooltip_text = kwargs.get("tooltip_text", None)
    messageWindow = gui.lookandfeel.tk.Toplevel(root)
    messageWindow.iconphoto(False, icon_photo)
    gui.windowmanagement.centered_window(messageWindow)
    messageWindow.title(str(title))
    messageWindow.geometry(str(width) + "x" + str(height))
    messageWindow.minsize(width, height)
    messageLabel = gui.lookandfeel.ttk.Label(
        messageWindow, text="\n" + str(message) + "\n", justify="center"
    )
    if tooltip_text:
        gui.tooltips.create_tooltip(messageLabel, text=str(tooltip_text))
    messageLabel.pack()
    messageConfirmButton = gui.lookandfeel.ttk.Button(
        messageWindow,
        text="OK",
        style="my.TButton",
        command=lambda: messageWindow.destroy(),
    )
    messageConfirmButton.pack()
    messageWindow.focus_force()
    gui.lookandfeel.apply_theme_to_titlebar(messageWindow)
    return -1

if __name__ == '__main__':
    pass