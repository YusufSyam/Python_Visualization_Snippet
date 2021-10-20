## Snippets for generating n unique random color from a given cmap

Recommended to use qualitative colormaps as cmap

List of available cmaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html , or do matplotlib.pyplot.colormaps()

##### get_random_cmap.py :

```python
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
```

Example: getting colors for a histogram, where the first histogram takes the color on cmap 'Dark2', and the second histogram with cmap 'Accent'

```python
from get_random_cmap import get_random_cmap
from matplotlib import pyplot as plt
import numpy as np
```

```python
x= [np.random.normal(3,10) for _ in range(100)]
y= [np.random.normal(3,10) for _ in range(100)]

plt.figure(figsize=(20,4))
plt.subplot(121)
plt.hist(x, color=get_random_cmap('Dark2', 1))

plt.subplot(122)
plt.hist(y, color=get_random_cmap('Accent', 1))
    
plt.show()
```

![ex1](https://user-images.githubusercontent.com/54948391/138048925-e06242a2-f32e-4026-bb6d-8d1c184d1a1f.png)

Second example: when you want colors from the same cmap and still keep them different from each other

```python
bars_num= 5

bar1= np.random.randint(3000,7000,bars_num)
bar2= np.random.randint(5000,9000,bars_num)
bar3= np.random.randint(7000,11000,bars_num)

width= 0.25
index= np.arange(bars_num)

random_color_list= get_random_cmap('Set3', 3)

plt.figure(figsize=(16,5))
plt.bar(index-width, bar1, width=width, color=random_color_list[0])
plt.bar(index, bar2, width=width, color=random_color_list[1])
plt.bar(index+width, bar3, width=width, color=random_color_list[2])

plt.show()
```

![ex2](https://user-images.githubusercontent.com/54948391/138049000-93564e0c-84cc-4781-a1b0-2da11edc55f0.png)

Another example

```python
plt.figure(figsize=(18,10))
for i in range(6):
    plt.subplot(2,3,i+1)
    
    num_of_slices= np.random.randint(2,5)
    slices= np.random.randint(10,50, num_of_slices)
    
    random_color_list= get_random_cmap('Set3', num_of_slices)
    plt.pie(slices, autopct='%1.1f%%', colors=random_color_list)
```

![ex3](https://user-images.githubusercontent.com/54948391/138049056-dfb2f11b-846e-428f-9df5-18fc2c12a1d2.png)
