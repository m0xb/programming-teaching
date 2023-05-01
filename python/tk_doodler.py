import tk_base

class DoodlerUI:

    def __init__(self):
        # The `app` attribute will be set in init_ui
        self.app = None
        self.window_size = None

        self.is_mouse_down = False
        self.mouse_last_pos = None
        self.mouse_color = 0

        self.color_palette_index = 0
        self.color_palettes = [
            [0xffffff],
            [0xff0000, 0xff8800, 0xffff00, 0x00ff00, 0x0000ff, 0xff00ff, 0xff0000],
            [0xff0000, 0x0000ff],
            [0xff0000, 0xff8000, 0xffff00, 0xff0000],
            [0x0000ff, 0x00ffff, 0x80ffff, 0x0000ff],
        ]

    def init_ui(self, app):
        self.app = app
        app.canvas.bind("<ButtonPress-1>", self.canvas_mouse_down)
        app.canvas.bind("<ButtonRelease-1>", self.canvas_mouse_up)
        app.canvas.bind("<B1-Motion>", self.canvas_move_mouse)
        app.main_window.bind("<Configure>", self.on_configure)
        self.draw_ui()

    def on_configure(self, event):
        new_window_size = (event.width, event.height)
        if new_window_size != self.window_size:
            print("Changed window size: {} -> {}".format(self.window_size, new_window_size))
            self.window_size = new_window_size
            self.draw_ui()

    def change_palette(self, app):
        self.color_palette_index = (self.color_palette_index + 1) % len(self.color_palettes)
        self.draw_ui()

    def reset(self, app):
        app.canvas.delete("all")
        self.draw_ui()

    def draw_ui(self):
        self.app.canvas.delete('ui')

        # seems that the width/height given by Tk returns some extra. E.g. 1206 returned vs 1200 real.
        canvas_w = self.app.canvas.winfo_width() - 6
        canvas_h = self.app.canvas.winfo_height() - 6
        #print("Canvas is {} x {}".format(canvas_w, canvas_h))
        pad = 5
        sqsz = 15
        num_colors = len(self.color_palettes)
        for row_idx, color_palette in enumerate(self.color_palettes):
            nth_from_bottom = num_colors - row_idx - 1
            ytop = canvas_h - pad*nth_from_bottom - sqsz*(nth_from_bottom+1)
            ybot = canvas_h - pad*nth_from_bottom - sqsz*nth_from_bottom
            if row_idx == self.color_palette_index:
                self.app.canvas.create_rectangle(
                    pad - 3, ytop - 3,
                    pad + (len(self.color_palettes[self.color_palette_index])) * sqsz + 3, ybot + 3,
                    fill='#FFFFFF', outline='', tags='ui')
            for col_idx, color in enumerate(self.color_palettes[row_idx]):
                self.app.canvas.create_rectangle(
                    pad + col_idx * sqsz, ytop,
                    pad + (col_idx + 1) * sqsz, ybot,
                    fill=self.int_to_hex_color(color), outline='', tags='ui')

    @staticmethod
    def int_to_hex_color(int_color):
        return f'#{int_color:06x}'

    def canvas_move_mouse(self, event):
        #print("moving mouse! event = {}, down = {}".format(event, self.is_mouse_down))

        def torgb(hex):
            r = (hex >> 16) & 0xff
            g = (hex >> 8) & 0xff
            b = (hex) & 0xff
            return r, g, b

        if False:
            r, g, b = torgb(self.mouse_color)
            delta = 10
            if b >= delta:
                b -= delta
            elif g >= delta:
                g -= delta
            elif r >= delta:
                r -= delta
            else:
                r = g = b = 0xff
            self.mouse_color = (r << 16) + (g << 8) + b
            actual_mouse_color = self.mouse_color
        else:
            from math import ceil, floor
            colors = self.color_palettes[self.color_palette_index]
            n_colors = len(colors)
            if self.mouse_color < 100:
                self.mouse_color += 1
            else:
                self.mouse_color = 0
            eff_idx = (self.mouse_color / 100) * (n_colors - 1)
            blend_color_a = colors[floor(eff_idx)]
            blend_color_b = colors[ceil(eff_idx)]
            a_pct = 1 - eff_idx % 1
            b_pct = eff_idx % 1
            print("val = {}, effective index = {}, color_a={:06x}, color_b={:06x}".format(self.mouse_color, eff_idx, blend_color_a, blend_color_b))
            # no blending
            #actual_mouse_color = blend_color_a
            # blending
            ra, ga, ba = torgb(blend_color_a)
            rb, gb, bb = torgb(blend_color_b)
            #print("ra,ga,ba = ({}, {}, {}), rb,gb,bb = ({}, {}, {})".format(ra, ga, ba, rb, gb, bb))
            actual_mouse_color = (int(ra*a_pct + rb*b_pct) << 16) + (int(ga*a_pct + gb*b_pct) << 8) + int(ba*a_pct + bb*b_pct)

        r, g, b = torgb(actual_mouse_color)
        print("rgb = ({}, {}, {}), hex={}".format(r, g, b, self.int_to_hex_color(actual_mouse_color)))
        self.app.canvas.create_line(self.mouse_last_pos[0], self.mouse_last_pos[1], event.x, event.y, fill=f'#{actual_mouse_color:06x}', width=3)
        self.mouse_last_pos = (event.x, event.y)

    def canvas_mouse_down(self, event):
        self.mouse_last_pos = (event.x, event.y)
        self.is_mouse_down = True
        print("MOUSE DOWN! event = {}, down = {}".format(event, self.is_mouse_down))

    def canvas_mouse_up(self, event):
        self.is_mouse_down = False
        print("MOUSE UP! event = {}, down = {}".format(event, self.is_mouse_down))


doodler_ui = DoodlerUI()
tk_base.TkBaseApp({
        "Change palette": doodler_ui.change_palette,
        "Reset": doodler_ui.reset
    },
    doodler_ui.init_ui
).run()
