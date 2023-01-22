import curses
from curses import wrapper


def main(stdscr):
    """
    The main function of this curses TUI (Textual User Interface) program

    :param stdscr: the root `window` object provided by curses which represents the text area on the terminal
    :return: None
    """

    stdscr.clear()

    # Create two windows, which we can swap between
    main_windows = [
        curses.newwin(10, 90, 0, 0),
        curses.newwin(5, 50, 1, 5),
    ]

    # Do a one-time, preliminary refresh on the stdscr.
    # See SO post. Basically, the getch will trigger a refresh if needed and the first refresh will clear the screen
    # (which would clear out the drawing we did in our windows).
    # https://stackoverflow.com/questions/67021267/python-curses-newwin-not-being-displayed-if-stdscr-hasnt-been-refreshed-first
    stdscr.refresh()

    # main_windows[0].bkgd('.')
    main_windows[0].border()
    main_windows[0].addstr(0, 3, "Window #1")
    main_windows[0].addstr(1, 2, "Curses is cool")

    # main_windows[1].bkgd(',')
    main_windows[1].border()
    main_windows[1].addstr(0, 3, "Window #2")
    main_windows[1].addstr(1, 2, "Math is also very cool too")

    # UI state vars:
    current_window_index = 0

    while True:
        # 1. Redraw
        # ---------------------------------------------------------------------
        # touchwin() invalidates the area covered by this window, making curses redraw content.
        main_windows[current_window_index].touchwin()
        # refresh() redraws the screen area covered by this window.
        # It applies all changes that have been made since the last refresh (I think?).
        main_windows[current_window_index].refresh()

        # 2. User input
        # ---------------------------------------------------------------------
        # Wait for a keypress to prevent the program from exiting
        ch = chr(stdscr.getch())
        if ch == 'q':
            break
        elif ch == ' ':
            current_window_index = (current_window_index + 1) % len(main_windows)


wrapper(main)
