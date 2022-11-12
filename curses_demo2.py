import curses

# wrong!:
#import dataclasses
# right:
from dataclasses import dataclass

from curses import wrapper


@dataclass
class Entity:
    # old skool:
    # def __init__(self, x: int, y: int, player_name: str):
    #     self.x = x
    #     self.y = y
    #     self.player_name = player_name

    # with dataclasses:
    x: int
    y: int
    name: str
    symbol: str
    value: int = 0


def main(stdscr):
    cur_team_index = 0
    teams = [f"BLUE", f"RED"]
    player = Entity(30, 3, "Sim", "S")

    powerups = [
        Entity(0, 5, "Elixir of Strength", 's', 100),
        Entity(50, 8, "Potion of Potency", 'p', 100),
        Entity(33, 4, "Test thingy", 't', 10),
    ]

    stdscr.clear()
    stdscr.refresh()
    # Hide the cursor
    curses.curs_set(0)

    # Define color pairs for use later on:
    # blue text on white background is color pair 1
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    # red text on white background is color pair 2
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    # Player color scheme
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)



    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "Team {} - your turn ".format(teams[cur_team_index]), curses.color_pair(cur_team_index+1))

        # Iterate over all powerups and draw each of them
        for powerup in powerups:
            stdscr.addstr(powerup.y, powerup.x, powerup.symbol)
            if player.x == powerup.x and player.y == powerup.y:
                stdscr.addstr(2, 0, "Pick up powerup? - {} (${})".format(powerup.name, powerup.value))
                stdscr.addstr(powerup.y + 1, powerup.x, "{} (${})".format(powerup.name, powerup.value))
                player.value += powerup.value
                powerups.remove(powerup)

        stdscr.addstr(1, 0, "Player - {}".format(player))

        # Draw the player at their current position
        stdscr.addstr(player.y, player.x, player.symbol, curses.color_pair(3))


        # getch() returns the ordinal value of the character typed, e.g. 97 for a lowercase 'a'
        ch_code = stdscr.getch()
        # convert the ordinal to a single-character string with chr()
        ch = chr(ch_code) # e.g. chr(97) -> 'a'
        if ch == 'q':
            break
        elif ch == 'w':
            player.y -= 1
        elif ch == 's':
            player.y += 1
        elif ch == 'a':
            player.x -= 1
        elif ch == 'd':
            player.x += 1

        # TODO: Add bounds check to player position. Otherwise, game crashes if player off screen.

        # Mystery: uncommenting the below line doesn't seem to change anything. So what does refresh() actually do?
        #stdscr.refresh()

        # increment current team
        # modulo by len(teams) so that it cycles through the defined teams
        # if only two teams, it'll go 0 -> 1 -> 0 -> 1 -> ...
        # if three, it'll go 0 -> 1 -> 2 -> 0 -> 1 -> 2 -> 0 -> ...
        cur_team_index = (cur_team_index + 1) % len(teams)

    pass


wrapper(main)