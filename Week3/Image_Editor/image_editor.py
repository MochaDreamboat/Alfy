from image_editor_helper import *
import copy

def divide_channels(image):
    image_to_edit = copy.deepcopy(image)
    rows = len(image_to_edit)
    columns = len(image_to_edit[0])
    channels = len(image_to_edit[0][0])

    return [ [[image_to_edit[j][k][i] for k in range(columns)] for j in range(rows)] for i in range(channels) ]