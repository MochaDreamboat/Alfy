from image_editor_helper import *
import copy

def divide_channels(image):
    image_to_divide = copy.deepcopy(image)
    rows = len(image_to_divide)
    columns = len(image_to_divide[0])
    channels = len(image_to_divide[0][0])

    return [ [[image_to_divide[j][k][i] for k in range(columns)] for j in range(rows)] for i in range(channels) ]

'''
Dimensions of channel list
[
  channel [row - [column-value]]
  channel []
  channel []
]
'''
def merge_channels(image):
  image_to_merge = copy.deepcopy(image)
  number_of_channels = len(image_to_merge)
  rows = len(image_to_merge[0])
  columns = len(image_to_merge[0][0])

  return [ [[image_to_merge[k][i][j] for k in range(number_of_channels)] for j in range(columns)] for i in range(rows) ]