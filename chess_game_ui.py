from tkinter import *
from tkinter import ttk

class GridWidget(Canvas):
    def __init__(self, n_rows, n_cols, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.shapes = [[[] for c in range(n_cols)] for r in range(n_rows)]
        self.imgs = {
            'pawn': {
                'black': PhotoImage(file='/Users/smm/Downloads/DanProgramming/chess_assets/pawn_black.png'),
                'white': PhotoImage(file='/Users/smm/Downloads/DanProgramming/chess_assets/pawn_white.png'),
            }
        }
        self.draw_grid()

    def clear_squares(self):
        for row in self.shapes:
            for col in row:
                for id in col:
                    self.delete(id)

    def on_click_filled(self, row, col, event):
        for id in self.shapes[row][col]:
            self.delete(id)

    def on_click_empty(self, row, col, event):
        #print("click at row={}, col={}, event={}".format(row, col, event))
        cw, ch = self.winfo_reqwidth(), self.winfo_reqheight()
        square_w = cw / self.n_cols
        square_h = ch / self.n_rows
        padding = 5

        def make_click_handler(r, c):
            return lambda event: self.on_click_filled(r, c, event)

        tag = 'shape{}x{}'.format(row, col)
        if True:
            img = self.imgs['pawn'][['white', 'black'][(self.n_cols * row + col + row % 2) % 2]]
            hpad = square_w - img.width()
            vpad = square_h - img.height()
            print("Img(w={}, h={}), Square(w={}, h={}), hpad={}, vpad={}".format(img.width(), img.height(), square_w, square_h, hpad, vpad))
            new_shape_id = self.create_image(
                (0 + col * square_w + img.width() / 2 + hpad / 2,
                 0 + row * square_h + img.height() / 2 + vpad / 2),
                image=img,
                tags=tag
            )
        else:
            new_shape_id = self.create_rectangle(
                0 + col * square_w + padding,
                0 + row * square_h + padding,
                0 + col * square_w + square_w - padding,
                0 + row * square_h + square_h - padding,
                outline='',
                fill='#00f',
                tags=tag
            )
        self.tag_bind(tag, '<Button-1>', make_click_handler(row, col))
        self.shapes[row][col].append(new_shape_id)

    def draw_grid(self):
        #print("DRAW GRID. W={}, H={}".format(self.winfo_reqwidth(), self.winfo_reqheight()))
        cw, ch = self.winfo_reqwidth(), self.winfo_reqheight()
        square_w = cw / self.n_cols
        square_h = ch / self.n_rows
        square_colors = ["black", "white"]

        def make_click_handler(r, c):
            return lambda event: self.on_click_empty(r, c, event)

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                tag = 'square{}x{}'.format(row, col)
                self.create_rectangle(
                    0 + col * square_w,
                    0 + row * square_h,
                    0 + col * square_w + square_w,
                    0 + row * square_h + square_h,
                    outline='',
                    fill=square_colors[(self.n_cols * row + col + row % 2) % len(square_colors)],
                    tags=tag)
                self.tag_bind(tag, '<Button-1>', make_click_handler(row, col))


class ChessGameUI:

    def __init__(self):
        self.board_dims = (600, 600)

        self.main_window = Tk()

        self.main_window.geometry("650x720")
        # Create a container that belongs to the main window
        container_frame = ttk.Frame(self.main_window, padding=10)
        #container_frame.grid()
        container_frame.pack()

        # Create two label widgets and assign to variables
        my_label1 = Label(container_frame, text="Game status label", bg="red", fg="black")
        my_label1.pack(fill=X)

        ttk.Button(container_frame, text="Clear grid", command=self.clear_grid).pack()
        #.grid(column=0, row=0)
        ttk.Button(container_frame, text="Quit", command=self.main_window.destroy).pack(fill=X)
        #.grid(column=1, row=0)

        # Maybe add highlightthickness=0 to fix excess margin/padding?
        # https://stackoverflow.com/questions/48129549/tkinter-remove-white-border-outside-canvas
        #self.canvas = Canvas(container_frame, bg="#f00", height=self.board_dims[1], width=self.board_dims[0])
        #self.canvas.pack(fill=BOTH, expand=True)
        self.grid = GridWidget(8, 8, container_frame, bg="#ff0", height=self.board_dims[1], width=self.board_dims[0])
        self.grid.pack(fill=BOTH, expand=True)

    def clear_grid(self):
        self.grid.clear_squares()

    def run(self):
        self.main_window.mainloop()


ChessGameUI().run()