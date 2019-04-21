import sys
import json
import random

json_input = {}

with open('input.json', 'r') as f:
    json_input = json.load(f)
    
with open('car.txt', 'w') as f:
    f.write('{\n')
    for triangle in json_input.values():
        for coor in triangle.values():
            f.write('\t')
            for i in range(3):
                f.write(str(round(coor[i]/2, 3)) + 'f, ')
            f.write('\t\t')
            for i in range(3):
                f.write(str(round(random.uniform(0.0, 1.0), 2)) + 'f, ')
            f.write('\t\t')
            f.write('0.5f, 0.5f,')
            f.write('\n')
        f.write('\n')
    f.write('};')