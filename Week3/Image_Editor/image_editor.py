from image_editor_helper import *
import copy

def divide_channels(image):
    image_to_divide = copy.deepcopy(image)
    rows = len(image_to_divide)
    columns = len(image_to_divide[0])
    channels = len(image_to_divide[0][0])

    return [ [[image_to_divide[j][k][i] for k in range(columns)] for j in range(rows)] for i in range(channels) ]

def merge_channels(image):
  image_to_merge = copy.deepcopy(image)

  