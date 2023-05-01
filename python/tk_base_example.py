import random
import tk_base

def draw(app):
    # Draw a randomly sized and positioned blue rectangle
    x = random.randint(1, 800)
    y = random.randint(1, 600)
    w = random.randint(1, 100)
    h = random.randint(1, 100)
    app.canvas.create_rectangle(x, y, x+w, y+h, fill="#00F", outline="#44F")

tk_base.TkBaseApp({"Draw a rectangle!": draw}).run()
