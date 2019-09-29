
import bpy
from mathutils import *
D = bpy.data
C = bpy.context

def add_shader(material: bpy.types.Material, start_color=(1, 1, 1, 1), end_color=(0, 0, 0, 1), shades=4):
    """Adds a toon shader to a material
    
    Arguments:
        material {Material} -- The material to add the shader to
    
    Keyword Arguments:
        start_color {tuple} -- One of the base colors of the shader (default: {(1, 1, 1, 1)})
        end_color {tuple} -- the other base color of the shader (default: {(0, 0, 0, 1)})
        shades {int} -- the number of shades to add (default: {4})
    """
    #obtains and creates the nodes necessary
    tree = material.node_tree
    to_RGB_node = tree.nodes.new("ShaderNodeShaderToRGB")
    color_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    outline_node = tree.nodes.new("ShaderNodeLayerWeight")
    outline_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    mix_node = tree.nodes.new("ShaderNodeMixRGB")

    #the links in the node tree
    links = tree.links

    #removes link from input to output
    material_link = links[0]
    output_socket = material_link.to_socket
    material_socket = material_link.from_socket
    links.remove(material_link)

    #creates new links
    links.new(output_socket, mix_node.outputs[0])
    #layer weight
    links.new(mix_node.inputs[1], outline_ramp_node.outputs[0])
    links.new(outline_ramp_node.inputs[0], outline_node.outputs[1])
    #shader to rgb
    links.new(mix_node.inputs[2], color_ramp_node.outputs[0])
    links.new(color_ramp_node.inputs[0], to_RGB_node.outputs[0])
    links.new(to_RGB_node.inputs[0], material_socket)

    #adds stops to the color ramp nodes
    add_colors(ramp=outline_ramp_node, shades=2, end_position=.6)
    add_colors(ramp=color_ramp_node, shades=shades, start_color=start_color, end_color=end_color, end_position=shades/(shades+1))
    #changes a mix shader to multiply
    mix_to_multiply(mix_node)


def add_colors(ramp: bpy.types.TextureNodeValToRGB, shades=2, start_color=(1, 1, 1, 1), end_color=(0, 0, 0, 1), end_position=0):
    """Adds color stops and constant interpolation to a color ramp node
    
    Arguments:
        ramp {bpy.types.TextureNodeValToRGB} -- The color ramp node to modify
    
    Keyword Arguments:
        shades {int} -- The number of colors you want in the color ramp node (default: {2})
        start_color {tuple} -- the starting color of the color ramp node (default: {(1, 1, 1, 1)})
        end_color {tuple} -- the ending color of the color ramp node (default: {(0, 0, 0, 1)})
        end_position {int} -- the position of the last handle (default: {0})
    
    Raises:
        ValueError: if there are less than two shades
    """
    if shades < 2:
        raise ValueError("shades cannot be less than 2")
    #changes interpolation to constant
    ramp.color_ramp.interpolation = "CONSTANT"
    color_stops = ramp.color_ramp.elements
    #sets the values of the default stops
    color_stops[0].color = start_color
    color_stops[1].position = end_position
    color_stops[1].color = end_color
    i = 2
    #adds more ColorRampElements
    while i<shades:
        location = (end_position)*((i-1)/(shades-1))
        element = ramp.color_ramp.elements.new(location)
        element.color = interpolate_color(i/shades, start_color, end_color)
        i += 1


def interpolate_color(combine_value: float, start_color=(1, 1, 1, 1), end_color=(0, 0, 0, 1)):
    """Interpolates a color based on two other colors and a value between 0 and 1
   
    Arguments:
        combine_value {float} -- The fraction to interpolate by. In the interval [0, 1]
   
    Keyword Arguments:
        start_color {tuple} -- RGBA value of the first color (default: {(0, 0, 0, 1)})
        end_color {tuple} -- RGBA value of the second color (default: {(1, 1, 1, 1)})
   
    Raises:
        ValueError: if combine_calue is not in [1, 0]
   
    Returns:
        tuple -- RGBA value of the interpolated color
    """
    if combine_value > 1 or combine_value < 0:
        raise ValueError("combine_value needs to be between 0 and 1")

    l = []
    n = 0

    while n < 4:
        toAdd = (end_color[n] - start_color[n]) * combine_value + start_color[n]
        l.append(toAdd)
        n += 1

    return tuple(l)


def mix_to_multiply(mix: bpy.types.ShaderNodeMixRGB):
    """Changes a Mix node to a multiuply Node
    """
    mix.blend_type = "MULTIPLY"
    mix.inputs[0].default_value = 1

