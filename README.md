# QuickToon
An script for Blender that sets up the nodes necessary for a toon shader

## Warning!
This script has only been tested using Eevee and the pricipled shader. The UI is still in development and does not work yet.

## How to use this script
The add_shader(material, start_color, end_color, shades) method from module quick_toon adds a toon shader to a material

### parameters
*material (bpy.types.material) - the material to add the shader to  
*start_color (tuple of size 4, default: (1, 1, 1, 1)) - The RGBA values (0-1) of one of the base colors of the shader  
*end_color (tuple of size 4, default: (0, 0, 0, 1)) - The RGBA values (0-1) of another one of the base colors of the shader  
*shades (integer, default: 4) - the number of shades in the toon shader  
