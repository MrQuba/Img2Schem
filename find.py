import math
import blocks

def distance_between_colors(hex1, hex2):
      r1, g1, b1 = int(hex1[1:3], 16), int(hex1[3:5], 16), int(hex1[5:7], 16)
      r2, g2, b2 = int(hex2[1:3], 16), int(hex2[3:5], 16), int(hex2[5:7], 16)
      distance = math.sqrt(((r2 - r1) ** 2) + ((g2 - g1) ** 2) + ((b2-b1) ** 2))
      return distance

def closest_color_in_map(hex):
       smallest_distance = float('inf')
       closest_block  = None
       for map_hex, map_block in blocks.hex_to_block_map.items():
             distance = distance_between_colors(hex, map_hex)
             if distance < smallest_distance:
                  smallest_distance = distance
                  closest_block = (map_hex, map_block) 
       return closest_block
