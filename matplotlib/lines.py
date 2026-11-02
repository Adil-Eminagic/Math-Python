import numpy as np
import matplotlib.pyplot as plt


# unpacking

nums = [11]

n, = nums

print(n)

pair = (4,3)

x,y = pair

print(x, ' ', y)


fig, ax = plt.subplots()

x = [1, 2, 3]

lines = ax.plot(
    x, [2, 4, 6], "r-",
    x, [3, 6, 9], "b-"
)

# ax.plot reicieves list od Line2d objects

# ax.plot() returns:

# [
#     Line2D(
#         x = [1, 2, 3],
#         y = [4, 5, 6],
#         label = "My line"
#     )
# ]

plt.show()
