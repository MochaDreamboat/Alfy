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
  channel [row - [column1-value, column2-value, etc.]]
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


def from_rgb_to_gray(image):
  RED_MULTIPLIER = 0.299
  GREEN_MULTIPLIER = 0.587
  BLUE_MULTIPLIER = 0.114

  image_to_gray = divide_channels(image)
  red_channels = image_to_gray[0]
  green_channels = image_to_gray[1]
  blue_channels = image_to_gray[2]

  # Modify vals in place for RGB (using respective factors for multiplication)
  for i in range(len(red_channels)):
    for j in range(len(red_channels[0])):
      red_channels[i][j] *= RED_MULTIPLIER
  
  for i in range(len(green_channels)):
    for j in range(len(green_channels[0])):
      green_channels[i][j] *= GREEN_MULTIPLIER
  
  for i in range(len(blue_channels)):
    for j in range(len(blue_channels[0])):
      blue_channels[i][j] *= BLUE_MULTIPLIER

  # Reassigned to image with modified RGBs
  image_to_gray = merge_channels(image_to_gray)

  # RGB lists within each row/column are summed and result takes its place
  for i in range(len(image_to_gray)):
    for j in range(len(image_to_gray[0])):
      image_to_gray[i][j] = round(sum(image_to_gray[i][j]))

  return image_to_gray