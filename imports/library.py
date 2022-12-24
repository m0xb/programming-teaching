

class Vec2:

    # Class attribute
    ZERO = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


UP = Vec2(0, 1)
DOWN = Vec2(0, -1)

#
# print("Zero is " + str(Vec2.ZERO))
#
# Vec2.ZERO
#
# a_vec = Vec2(1,1)
# a_vec.x
#
# b_vec = Vec2(2,2)
# b_vec.x