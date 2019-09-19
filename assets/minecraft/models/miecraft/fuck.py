file_list = [
    'light_shell',
    'bio_essence',
    'glue',
    'cooling_block',
    'yellow_energy_block',
    'fibre',
    'sap',
    'solid_fuel',
    'metal_fastener',
    'prismarine_baffle',
    'obsidian_crystal',
    'blue_energy_block',
    'heavy_shell',
    'wooden_handle',
    'red_energy_block',
    'clear_ender_glass',
]




content = '''{{
    "parent": "item/generated",
    "textures": {{
        "layer0": "miecraft/{}"
    }}
}}
'''

for name in file_list:
    with open(name+'.json', 'w') as f:
        f.write(content.format(name))