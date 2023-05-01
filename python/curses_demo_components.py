import curses

from curses import wrapper
from pathlib import Path


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
        self.window.erase()
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

    EVENT_TYPE_SUBMIT = 'submit'
    EVENT_TYPE_CANCEL = 'cancel'

    def __init__(self, window, prompt, event_handler):
        """
        :param window: The backing curses window that this component will use
        :param prompt: The prompt to show the user, e.g. "Input: "
        :param event_handler: A function which takes two parameters (event_type: str, event_data: dict) and is called
          when the user completes their interaction with this component
        """
        super().__init__(window)
        self.prompt = prompt
        self.event_handler = event_handler
        self.input_text = ''

    def reset(self) -> None:
        """
        Clear out any text the user has entered
        """
        # Update the text we've stored
        self.input_text = ''
        # And don't forget to erase the curses window!
        self.window.erase()

    def refresh(self):
        self.set_text(self.prompt + self.input_text)
        super().refresh()

    def handle_input(self, char_code: int) -> bool:
        char = chr(char_code)
        if char_code == curses.KEY_ENTER or char == '\n':  # wtf, what is KEY_ENTER for? numpad?
            # If the user presses enter, then inform the event handler they want to submit the text
            self.event_handler(self.EVENT_TYPE_SUBMIT, {'text': self.input_text})
        elif char_code == 27:  # ESC
            # If the user pressed escape, then they want to cancel the text input
            self.event_handler(self.EVENT_TYPE_CANCEL, {})
        elif char_code == curses.KEY_BACKSPACE or char_code == 127:  # needs 127 for mac https://stackoverflow.com/questions/47481955/python-curses-detecting-the-backspace-key
            # Backspace one character
            self.input_text = self.input_text[:-1]
        else:
            # Regular character, append it
            self.input_text += char
        return True


def main(stdscr):
    """
    The main function of this curses TUI (Textual User Interface) program

    :param stdscr: the root `window` object provided by curses which represents the text area on the terminal
    :return: None
    """

    # Define an event handler for the text input
    def event_handler(event_type, event_data):
        nonlocal active_component
        if event_type == 'cancel':
            # If we got a cancel event, then go back to the main window
            active_component = main_window
        elif event_type == 'submit':
            # If the user submitted a file name, try to load it and show the contents in the popup
            file_name = event_data['text']
            cur_dir = Path(__file__).parent
            path_to_open = cur_dir / file_name
            if path_to_open.exists():
                if path_to_open.is_file():
                    with open(path_to_open, 'r') as f:
                        popup_window.set_text(str(path_to_open) + "\n\n" + f.read())
                else:
                    popup_window.set_text("Not a file: " + str(path_to_open))
            else:
                popup_window.set_text("Not found: " + str(path_to_open))
            active_component = popup_window
        else:
            # Unknown event type
            # TODO: Add better error handling!
            popup_window.set_text("GOT UNKNOWN EVENT: {} {} file={}".format(event_type, event_data, __file__))

    # Create the components in our UI
    main_window = BorderedComponent(curses.newwin(10, 90, 0, 0))
    main_window.set_text("Main Window\nCurses is cool\n\nControls:\n[  o  ] - open file\n[  q  ] - quit\n[space] - file viewer")

    popup_window = BorderedComponent(curses.newwin(5, 50, 2, 5))
    popup_window.set_text("File Viewer\n(no file loaded)")

    file_input = TextInputComponent(curses.newwin(5, 50, 2, 5), "File name: ", event_handler)

    # UI state vars:
    active_component = main_window

    # Do a one-time, preliminary refresh on the stdscr.
    # See SO post. Basically, the getch will trigger a refresh if needed and the first refresh will clear the screen
    # (which would clear out the drawing we did in our windows).
    # https://stackoverflow.com/questions/67021267/python-curses-newwin-not-being-displayed-if-stdscr-hasnt-been-refreshed-first
    stdscr.refresh()

    while True:
        # 1. Redraw
        # ---------------------------------------------------------------------
        # touchwin() invalidates the area covered by this window, making curses redraw content.
        active_component.touchwin()
        # refresh() redraws the screen area covered by this window.
        # It applies all changes that have been made since the last refresh (I think?).
        active_component.refresh()

        # 2. User input
        # ---------------------------------------------------------------------
        # Get the key pressed by the user
        char_code = stdscr.getch()
        # Let the active component react to the key press
        handled = active_component.handle_input(char_code)
        # If it didn't handle it, then use fallback to the main screen controls
        if not handled:
            if chr(char_code) == 'q':
                break
            elif chr(char_code) == 'o':
                file_input.reset()
                active_component = file_input
            elif chr(char_code) == ' ':
                active_component = main_window if active_component == popup_window else popup_window


wrapper(main)
