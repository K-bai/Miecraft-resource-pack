content = '''{{
    "parent": "item/generated",
    "textures": {{
        "layer0": "miecraft/magic_pot/{}/{:d}"
    }}
}}'''

import os

list = ('white','orange','magenta','light_blue','yellow','lime','pink','gray','light_gray','cyan','purple','blue','brown','green','red','black')

for t in list:
    os.mkdir(t)
    for i in range(8):
        with open(os.path.join(t, '{:d}.json'.format(i)), 'w') as f:
            f.write(content.format(t, i))