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

    def handle_input(self, char_code: int) -> bool:
        """
        Called when this component is active and the user presses a key
        :param char_code: the key code of the pressed key
        :return: true if this component acted on the input
        """
        return False

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


class TextInputComponent(BorderedComponent):
    def handle_input(self, char_code: int) -> bool:
        self.set_text("Input: [ {} ]".format((chr(char_code))))
        return True


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
        TextInputComponent(curses.newwin(5, 50, 2, 5)),
    ]

    # Do a one-time, preliminary refresh on the stdscr.
    # See SO post. Basically, the getch will trigger a refresh if needed and the first refresh will clear the screen
    # (which would clear out the drawing we did in our windows).
    # https://stackoverflow.com/questions/67021267/python-curses-newwin-not-being-displayed-if-stdscr-hasnt-been-refreshed-first
    stdscr.refresh()

    main_components[0].set_text("Window #1\nCurses is cool\n\nControls:\no       - open file\nq       - quit\n[space] - popup")
    main_components[1].set_text("Window #2\nMath is also very cool too, as well")
    main_components[2].set_text("File name: ")

    # UI state vars:
    active_component_index = 0

    while True:
        # 1. Redraw
        # ---------------------------------------------------------------------
        # touchwin() invalidates the area covered by this window, making curses redraw content.
        main_components[active_component_index].touchwin()
        # refresh() redraws the screen area covered by this window.
        # It applies all changes that have been made since the last refresh (I think?).
        main_components[active_component_index].refresh()

        # 2. User input
        # ---------------------------------------------------------------------
        # Wait for a keypress to prevent the program from exiting
        char_code = stdscr.getch()

        handled = main_components[active_component_index].handle_input(char_code)
        if not handled:
            if chr(char_code) == 'q':
                break
            elif chr(char_code) == 'o':
                active_component_index = 2
            elif chr(char_code) == ' ':
                active_component_index = 1
        # elif ch == ' ':
        #     active_component_index = (active_component_index + 1) % len(main_components)
        #



wrapper(main)
