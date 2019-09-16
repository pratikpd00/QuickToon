import bpy
from mathutils import *
from bpy.types import (Material, Node, NodeTree)
D = bpy.data
C = bpy.context

def toonify():
    for m in D.materials:
        add_shader(m)

def add_shader(material: Material):
    tree = material.node_tree
    to_RGB_node = tree.nodes.new("ShaderNodeShaderToRGB")
    color_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    outline_node = tree.nodes.new("ShaderNodeLayerWeight")
    outline_ramp_node = tree.nodes.new("ShaderNodeValToRGB")
    mix_node = tree.nodes.new("ShaderNodeMixRGB")



toonify()