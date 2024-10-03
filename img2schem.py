from PIL import Image
import numpy as np
import find
from litemapy import Schematic, Region, BlockState
# Colors of result might not be fully accurate
def rgb_to_hex(pixel):
        return "#{:02x}{:02x}{:02x}".format(pixel[0], pixel[1], pixel[2])

file_name = "image.png" # change it to convert different image
img = Image.open(file_name)

vertical = True # change it to False if you want schematic to be horizontal

img_array = np.array(img)
height, width, channels = img_array.shape
if vertical == False:
     region = Region(0,0,0, width, 1, height)
else:
     region = Region(0,0,0, width, height, 1 )
schem = region.as_schematic(name="Image", author="MrQuba", description="Made with litemapy")

for i in range(height):
    for j in range(width):
         pixel = img_array[i, j]
         hex, block = find.closest_color_in_map(rgb_to_hex(pixel))
         block = BlockState(block)
         if vertical == False:
             region[j, 0, i] = block
         else:
             region[j, i, 0] = block

schem.save("image.litematic")
