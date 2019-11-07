import sys
import numpy as np
import matplotlib.pyplot as plt

class Imageprocessor:
    def load(path):
        img = plt.imread(path)
        print ("Loading image of dimensions " + str(len(img[0])) + ' x ' + str(len(img[1])))
        return img
    def display(path):
        plt.imshow(path)
        plt.show
        
arr = Imageprocessor.load("42AI.png")
Imageprocessor.display(arr)