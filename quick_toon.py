import bpy
from mathutils import *
from bpy.types import (Material)
D = bpy.data
C = bpy.context

def toonify():
    for m in D.materials:
        add_shader(m)

def add_shader(material: Material):
    """Takes a material and adds nodes to it to make it a toon shader
    
    Arguments:
        material {Material} -- The material to make into a toon shader
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


def add_shades(ramp: bpy.types.TextureNodeValToRGB, shades=2, start_shade=(0, 0, 0, 1), end_shade=(1, 1, 1, 1)):
    #changes interpolation to constant
    ramp.color_ramp.interpolation = "CONSTANT"
    i = 1
    color_stops = ramp.color_ramp.elements
    color_stops[0].color = start_shade
    color_stops[1].color = end_shade
    while i<shades:
        element = ramp.color_ramp.elements.new(i/shades)
        element.color = interpolate_color(i/shades, start_shade, end_shade)
        i += 1


def interpolate_color(combine_value: float, start_color=(0, 0, 0, 1), end_color=(1, 1, 1, 1)):
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
        n+=1

    return tuple(l)



toonify()