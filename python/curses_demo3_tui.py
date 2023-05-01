import curses
from curses import wrapper


def main(stdscr):
    cur_team_index = 0
    teams = [f"BLUE", f"RED"]

    stdscr.clear()
    stdscr.refresh()

    # Define color pairs for use later on:
    # blue text on white background is color pair 1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    # red text on white background is color pair 2
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    while True:
        #stdscr.clear()

        stdscr.addstr(0, 0, "Team {} - your turn ".format(teams[cur_team_index]), curses.color_pair(cur_team_index+1))

        # getch() returns the ordinal value of the character typed, e.g. 97 for a lowercase 'a'
        ch_code = stdscr.getch()
        # convert the ordinal to a single-character string with chr()
        ch = chr(ch_code) # e.g. chr(97) -> 'a'
        if ch == 'q':
            break
        stdscr.addstr(3, 20, "You typed '{}'".format(ch))
        # Mystery: uncommenting the below line doesn't seem to change anything. So what does refresh() actually do?
        #stdscr.refresh()

        # increment current team
        # modulo by len(teams) so that it cycles through the defined teams
        # if only two teams, it'll go 0 -> 1 -> 0 -> 1 -> ...
        # if three, it'll go 0 -> 1 -> 2 -> 0 -> 1 -> 2 -> 0 -> ...
        cur_team_index = (cur_team_index + 1) % len(teams)

    pass


wrapper(main)