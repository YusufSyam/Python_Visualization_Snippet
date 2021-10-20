# import the required libraries
from matplotlib import cm, colors
from matplotlib.pyplot import colormaps
from numpy import random

def get_random_cmap(choose_cmap='Set2', color_num=1):
    # checks if choose_cmap is a valid cmap
    if (choose_cmap not in colormaps()):
        print(f'{choose_cmap} is not a valid value for cmap, setting cmap to default cmap value..')

        # set the value of choose_cmap to be the same as default value
        choose_cmap = get_random_cmap.__defaults__[0]

    # setting the cmap
    cmap = cm.get_cmap(choose_cmap)

    # setting replace to false means that the colors will be unique to each other
    replace = False

    # gives condition, if color_num is greater than the number of colors in cmap, then replace is set to True
    if (color_num > cmap.N):
        print('color is not unique anymore because color_num is bigger than cmap length')
        replace = True

    # generates a random sample in the form of a 1d array from 0 to a-1 along size
    color_index = random.choice(a=cmap.N, size=color_num, replace=replace)

    # returns color in string if color_num is only 1, otherwise in a form of list
    return colors.rgb2hex(cmap(color_index)) if (color_num == 1) else [colors.rgb2hex(cmap(ci)) for ci in color_index]
