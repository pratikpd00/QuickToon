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
    #removes link from input to output
    tree.links.remove(tree.links[0])



    


toonify()