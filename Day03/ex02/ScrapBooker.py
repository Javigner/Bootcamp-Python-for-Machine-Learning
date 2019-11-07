import numpy as np
import sys
from ImageProcessor import Imageprocessor as imp


class Scrapbooker:
    def crop(array, dimensions, position):
        width = len(array[0])
        height = len(array[1])
        if (width <= dimensions[0] or height <= dimensions[1] or position[0] + dimensions[0] >= width or position[1] + dimensions[1] >= height):
            sys.exit("Dimensions is larger than the current image size.")
        return array[position[0]:width - dimensions[0],position[1]:height - dimensions[1]]
    def thin(array, n, axis):
        i = 0     
        if (n % 2 == 0):
            add = 1
        else:
            add = 0
        if (n == 1):
            return np.array([])
        if (n == 0):
            return array
        if (axis == 0):
            j = array.shape[1] - add
            result = array
            while (i < j):
                if (i % (n - 1) == 0 and i != 0):
                    result = np.delete(result, i, 1)
                    j -= 1
                i += 1
        if (axis == 1):
             j = array.shape[0] - add + 1
             result = array
             while (i < j):
                if (i % (n - 1) == 0 and i != 0):
                    result = np.delete(result, i, 0)
                    j -= 1
                i += 1
        return result