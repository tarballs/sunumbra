# testbuild.py
"""
collection of things that will eventually move to their own modules
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, floor, pi

# plt.matshow()
# plt.show()


class VisualArrayEditor:  # [y][x] deal wid it
    """ VAE
    facilitates creating a new world map, also contains tool-methods that may be better as separate pkg
    methods:
        draw() = helps other methods to modify an image array 'manually'
        walk_random() = used for creating a base landmass during world gen
        walk_guided() = several options for guiding the walker
    """
    def __init__(self, ylen, xlen):
        """
        args:
            ylen, xlen = dimensions of the array
        """
        self.ylen = ylen
        self.xlen = xlen
        self.xpos = 0
        self.ypos = 0
        self.ray = np.zeros((self.ylen, self.xlen, 3), dtype=np.uint8)

    def test(self, x):
        for i in range(0, x):
            self.walk_random([60, 60, 60], 0)

        plt.imshow(self.ray)
        plt.show()

    def test2(self):
        self.test(1)
        self.draw(self.ray, [100, 100], color='red')
        plt.imshow(self.ray)
        plt.show()

    def calculate_dist(self, p1, p2, round_down=True):  # !move to another package with other common tools!
        dist = sqrt(abs(p2[1] - p1[1]) ** 2 + abs(p2[0] - p1[0]) ** 2)
        if round_down:
            dist = floor(dist)
        return dist

    def draw(self, on, where, color='red', opt='circle', radius=7):  # odd numbers please
        """
        opt:
            'circle' = draws a circle on array at a chosen point
        args:
            on = 2d array
            where = [y, x]  # center of shape on the thing you are drawing to
            color = 'string'
        """
        if opt == 'circle':
            if color == 'red':  # !color chooser might be a nifty function to have in the future!
                color = [255, 0, 0]
                pass
            size = radius*3
            circle = [[0 for x in range(size)] for y in range(size)]  # inits array
            center_temp = size//2
            center = [center_temp, center_temp]
            for y in range(0, size):
                for x in range(0, size):
                    dist = self.calculate_dist([y, x], center)  # iters array, compares dist to radius of circle
                    if dist <= radius:
                        circle[y][x] = 1
            y, x = center[0], center[1]  # draws shape on the array
            y_adjustment, x_adjustment = abs(y - where[0]), abs(x - where[1])  # adjust puts cursor in tl corner
            for y in range(0, size):
                for x in range(0, size):  # iters circle and draws on array
                    pixel = circle[y][x]
                    if pixel == 1:
                        on[y + y_adjustment][x + x_adjustment] = color

    def randomize(self, opt=1):  # defaults are [9, 9]
        """
        scrambles various private vars, uses basic rand int. does not provide for weighted choice
        opt:
            1 randomize self.y/xpos
            2 no idea
        """
        if opt == 1:  # new ranom point index that exists in self.ray, with padded edges
            self.ypos = random.randint(9, self.ylen - 9)
            self.xpos = random.randint(9, self.xlen - 9)

        if opt == 2:  # no idea what this does
            ylowhi, xlowhi = [], []
            # , circlebrush=True, brushsize=12
            self.ypos = random.randint(ylowhi[0], ylowhi[1] )
            self.xpos = random.randint(9, self.xlen - 9)

    def walk_random(self, color, gate=0, opt=1, yposlow=9, yposhi=9, xposlow=9, xposhi=9):
        """
        wanders randomly, currently just for creating initial landmasses
        opt:
            1 basic random walker
        args:
            color = [int, int, int]
            gate = int  # set to non-zero value when trying to layer walks ontop of eachother
        """
        if opt == 1:
            self.randomize()  # gets a random starting point
            while True:
                if self.ypos < yposlow or self.ypos > self.ylen - yposhi:  # keeps from wandering out of bounds
                    break
                if self.xpos < xposlow or self.xpos > self.xlen - xposhi:
                    break
                while True:
                    point = self.ray[self.ypos, self.xpos]  # point is the 'walker' that draws a pixel if > gate
                    if sum(point) >= gate:
                        self.ray[self.ypos+1, self.xpos-1] = color  # this is the shape/brush that draws on array
                        self.ray[self.ypos-1, self.xpos+1] = color  # currently forms and 'x' shape
                        self.ray[self.ypos+1, self.xpos+1] = color  # there's two of them to draw a more solid shape
                        self.ray[self.ypos-1, self.xpos-1] = color
                        self.ray[self.ypos+2, self.xpos] = color
                        self.ray[self.ypos-2, self.xpos] = color
                        self.ray[self.ypos, self.xpos] = color
                        break
                    if sum(point) > 0:
                        self.ray[self.ypos+1, self.xpos-1] = color
                        self.ray[self.ypos-1, self.xpos+1] = color
                        self.ray[self.ypos+1, self.xpos+1] = color
                        self.ray[self.ypos-1, self.xpos-1] = color
                        self.ray[self.ypos+2, self.xpos] = color
                        self.ray[self.ypos-2, self.xpos] = color
                        self.ray[self.ypos, self.xpos] = color
                        break
                    else:
                        break
                # randomly chooses a direction for the walked to take a step in
                direct = random.choices(['n', 's', 'e', 'w'], weights=[0.25, 0.25, 0.25, 0.25], k=1)
                if direct[0] == 'n':
                    self.ypos -= 1
                    continue
                if direct[0] == 's':
                    self.ypos += 1
                    continue  # !not sure if to use break or continue!
                if direct[0] == 'e':
                    self.xpos += 1
                    continue
                if direct[0] == 'w':
                    self.xpos -= 1
                    continue

    def walk_guided(self, opt=1, prob_circles=3):
        """
        opt:
            1 = scaters island 'probability circles' on map, guides walker back towards circle the farther it gets away
                    from the center of the circle
        """
        if opt == 1:
            points = []
            for i in range(0, prob_circles):
                self.randomize()
                points.append([self.ypos, self.xpos])
                self.ray[self.ypos, self.xpos] = 000


# START !remove!
rt = VisualArrayEditor(250, 500)  # y,x deal wid it
rt.test2()
