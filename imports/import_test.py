# Option 1:
# import library
#
# my_vec = library.Vec2(5, 1)
# print(my_vec.x)
# print(library.UP)
# print(library.DOWN)

# Option 2:
# from library import *
#
# my_vec = Vec2(5, 1)
# print(my_vec.x)
# print(UP)
# print(DOWN)


# Option 2a:
# from library import Vec2, UP, DOWN
#
# my_vec = Vec2(5, 1)
# print(my_vec.x)
# print(UP)
# print(DOWN)

# Option 1a:
# import library as ballsack
#
# my_vec = ballsack.Vec2(5, 1)
# print(my_vec.x)
# print(ballsack.UP)
# print(ballsack.DOWN)

## Nested imports!

import subdir.more_library
import subdir.deeper.extra_library

# Sim is surprised that "subdir." is needed!
print(subdir.more_library.VecUtils.normalize())
print(subdir.deeper.extra_library.FOO)

# Does not work!
#   AttributeError: module 'subdir.more_library' has no attribute 'deeper'
#print(subdir.more_library.deeper.FOO)
# Sim does not know how to code herp derp ...


import subdir.deeper.extra_library as el
print(el.FOO)


