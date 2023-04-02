import tk_base

class DoodlerUI:

    def __init__(self):
        # The `app` attribute will be set once the user clicks reset... sucky, I know
        self.app = None

        self.is_mouse_down = False
        self.mouse_last_pos = None
        self.mouse_color = 0

    def reset(self, app):
        self._do_initial_event_setup(app)
        app.canvas.delete("all")

    def _do_initial_event_setup(self, app):
        if not self.app:
            print("Setting up events!")
            self.app = app
            app.canvas.bind("<ButtonPress-1>", self.canvas_mouse_down)
            app.canvas.bind("<ButtonRelease-1>", self.canvas_mouse_up)
            app.canvas.bind("<B1-Motion>", self.canvas_move_mouse)

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
            colors = [0xff0000, 0x0000ff]
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
            actual_mouse_color = (int(ra*a_pct + rb*b_pct) << 16) + (int(ga*a_pct + gb*b_pct)//2 << 8) + int(ba*a_pct + bb*b_pct)

        r, g, b = torgb(actual_mouse_color)
        print("rgb = ({}, {}, {}), hex={}".format(r, g, b, f'#{actual_mouse_color:06x}'))
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
tk_base.TkBaseApp({"Reset": doodler_ui.reset}).run()
