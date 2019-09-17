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
    output_node = tree.nodes[tree.active_output]
    material_node = tree.nodes[tree.active_input]
    to_RGB_node = tree.nodes.new("ShaderNodeShaderToRGB")
    color_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    outline_node = tree.nodes.new("ShaderNodeLayerWeight")
    outline_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    mix_node = tree.nodes.new("ShaderNodeMixRGB")

    #the links in the node tree
    links = tree.links

    #removes link from input to output
    material_link = links[0]
    material_socket = material_link.from_socket
    links.remove(material_link)

    #creates new links
    links.new(output_node.inputs[0], mix_node.outputs[0])
    #layer weight
    links.new(mix_node.inputs[1], outline_ramp_node.outputs[0])
    links.new(outline_ramp_node.inputs[0], outline_node.outputs[1])
    #shader to rgb
    links.new(mix_node.inputs[2], color_ramp_node.outputs[0])
    links.new(color_ramp_node.inputs[0], to_RGB_node.outputs[0])
    links.new(to_RGB_node.inputs[0], material_socket)



    


toonify()