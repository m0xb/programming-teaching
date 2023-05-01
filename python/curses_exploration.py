import curses
from curses import wrapper


def main(stdscr):
    curses.curs_set(0)
    # Apparently you gotta refresh the screen first before the pad will show...
    # https://stackoverflow.com/questions/25268526/pythons-curses-module-does-not-refresh-pad-until-first-character-received/26305933#26305933
    stdscr.refresh()

    stdscr.addstr(0, 0, "Curses {} x {}".format(curses.LINES, curses.COLS))
    stdscr.addstr(1, 0, "type(stdscr) = {}".format(type(stdscr)))
    stdscr.addstr(2, 0, "." * (curses.COLS - 0))



    pad = curses.newpad(100, 100)
    for y in range(0, 99):
        for x in range(0, 99):
            #pad.addch(y, x, ord('s') + (x*x+y*y) % 26)
            pad.addch(y, x, ' ')

    stdscr.addstr(3, 0, "type(pad) = {}".format(type(pad)))

    viewport_x = 0
    viewport_y = 0
    x = 0
    y = 0
    dots = []
    with open(__file__) as fh:
        code_lines = list(enumerate(fh.readlines()))

    while True:
        # Redraw the screen
        pad.refresh(viewport_y, viewport_x, 5,0, curses.LINES-1,75)

        # Get input from user
        ch_code = stdscr.getch()

        # Modify state
        if ch_code == curses.KEY_RIGHT:
            x += 1
        elif ch_code == curses.KEY_LEFT:
            x -= 1
            if x < 0:
                x = 0
        elif ch_code == curses.KEY_DOWN:
            y += 1
        elif ch_code == curses.KEY_UP:
            y -= 1
            if y < 0:
                y = 0

        ch = chr(ch_code) # e.g. chr(97) -> 'a'
        if ch == 'q':
            break
        elif ch == ' ':
            dots.append((y, x))
        elif ch == 'h':
            viewport_x -= 1
            if viewport_x < 0:
                viewport_x = 0
        elif ch == 'l':
            viewport_x += 1
        elif ch == 'j':
            viewport_y -= 1
            if viewport_y < 0:
                viewport_y = 0
        elif ch == 'k':
            viewport_y += 1
        else:
            stdscr.addstr(4, 0, "lol wut? ch_code = {}".format(ch_code))

        # Update screen state
        pad.erase()
        for pad_line in range(pad.getmaxyx()[0]):
            pad.addstr(pad_line, 0, str(pad_line))
        for line_no, code_line in code_lines:
            pad.addstr(line_no, 2, code_line)
        for dot in dots:
            pad.addch(dot[0], 2 + dot[1], '.')
        pad.addch(y, 2 + x, 'x')




wrapper(main)
