import curses
from curses import wrapper


class Component:

    def __init__(self, window: curses.window):
        self.window = window

    def _get_top_left_yx(self) -> (int, int):
        """
        Internal helper function to return the top left coordinate. This is used to draw text at the appropriate
        location within this component.
        :return: The top left coordinate as a 2-tuple of ints: (row, col)
        """
        return (0, 0)

    def set_text(self, text: str) -> None:
        lines = text.split('\n')
        top, left = self._get_top_left_yx()
        for idx, line in enumerate(lines):
            self.window.addstr(top + idx, left, line)

    def touchwin(self) -> None:
        self.window.touchwin()

    def refresh(self) -> None:
        raise Exception("Abstract method, subclasses must implement!")


class PlainComponent(Component):

    def refresh(self) -> None:
        self.window.refresh()


class BorderedComponent(Component):

    def _get_top_left_yx(self) -> (int, int):
        return (1, 1)

    def refresh(self):
        self.window.border()
        self.window.refresh()


def main(stdscr):
    """
    The main function of this curses TUI (Textual User Interface) program

    :param stdscr: the root `window` object provided by curses which represents the text area on the terminal
    :return: None
    """

    stdscr.clear()

    # Create the list of components in our UI
    main_components = [
        BorderedComponent(curses.newwin(10, 90, 0, 0)),
        BorderedComponent(curses.newwin(5, 50, 2, 5)),
    ]

    # Do a one-time, preliminary refresh on the stdscr.
    # See SO post. Basically, the getch will trigger a refresh if needed and the first refresh will clear the screen
    # (which would clear out the drawing we did in our windows).
    # https://stackoverflow.com/questions/67021267/python-curses-newwin-not-being-displayed-if-stdscr-hasnt-been-refreshed-first
    stdscr.refresh()

    main_components[0].set_text("Window #1\nCurses is cool")
    main_components[1].set_text("Window #2\nMath is also very cool too, as well")

    # UI state vars:
    active_component_index = 0

    while True:
        # 1. Redraw
        # ---------------------------------------------------------------------
        # refresh() redraws the screen area covered by this window.
        # It applies all changes that have been made since the last refresh (I think?).
        main_components[active_component_index].refresh()

        # 2. User input
        # ---------------------------------------------------------------------
        # Wait for a keypress to prevent the program from exiting
        ch = chr(stdscr.getch())
        if ch == 'q':
            break
        elif ch == ' ':
            active_component_index = (active_component_index + 1) % len(main_components)
            # touchwin() invalidates the area covered by this window, making curses redraw content.
            main_components[active_component_index].touchwin()


wrapper(main)
