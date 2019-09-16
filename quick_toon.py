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
    tree.nodes.new("ShaderNodeShaderToRGB")

toonify()