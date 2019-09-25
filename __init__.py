import bpy
from quick_toon import add_shader
from bpy.props import FloatVectorProperty, IntProperty

bl_info = {
    "name": "QuickToon",
    "author": "Pratik Deolasi",
    "description": "An addon that quickly generates toon shaders",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Generic"
}

class GenerateShaderOperator(bpy.types.Operator):
    bl_idname = "object.generateshader"
    bl_label = "Generate shader"

    start_shade: FloatVectorProperty(
        name="start_shade",
        description="The RGBA values of the starting color",
        size=4,
        default=(1, 1, 1, 1)
    )

    end_shade: FloatVectorProperty(
        name="end_shade",
        description="the RGBA values of the ending color",
        size=4,
        default=(0, 0, 0, 1)
    )

    shades: IntProperty(
        name="shades",
        description="the number of shades in the shader",
        soft_min=2,
        soft_max=10
    )

    def execute(self, context):
        add_shader(material=context.material, start_color=self.start_shade, end_color=self.end_shade, shades=self.shades)
        return {'FINISHED'}

def register():
    ...


def unregister():
    ...
