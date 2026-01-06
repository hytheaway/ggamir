# String operations

def shorten_file_name(old_filename: str, num_shown_char: int):
    # TODO: REVISIT, you know better ways to do this.
    """
    Takes a long string and shortens it to the length provided before appending ellipses.

    Args:
        old_filename (str): Full length filename to be shortened.
        num_shown_char (int): Number of letters from the old filename to show before inserting ellipses.

    Returns:
        str: Shortened version of the full filename to be shown with ellipses added.
    """
    if len(old_filename) > 17:
        old_filename = old_filename
        new_filename = str(old_filename[: int(num_shown_char)]) + "..."
    else:
        new_filename = old_filename
    return new_filename

if __name__ == '__main__':
    pass