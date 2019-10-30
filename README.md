# QuickToon
An script for Blender that sets up the nodes necessary for a toon shader

## Warning!
This addon only works with eevee. Color data such as textures do not work as intended yet.

## How to generate a toon shader using the GUI
This addon adds a panel called "Generate toon shader" to the material tab of the properties editor. To add a toon shader to a mesh, have the mesh selected, and click on
Generate shader in the new panel. This will bring up a popup that allows you to chose the two colors that will be used in the toon shader, and the number of different shades that 
will be used in the shader. After you are done modifying these values, click ok, and the addon will automatically add the nodes necessary for a toon shader.

## How to generate a toon shader by scripting
The add_shader(material, start_color, end_color, shades) method from module quick_toon adds a toon shader to a material

### parameters
* material (bpy.types.material) - the material to add the shader to  
* start_color (tuple of size 4, default: (1, 1, 1, 1)) - The RGBA values (0-1) of one of the base colors of the shader  
* end_color (tuple of size 4, default: (0, 0, 0, 1)) - The RGBA values (0-1) of another one of the base colors of the shader  
* shades (integer, default: 4) - the number of shades in the toon shader  
