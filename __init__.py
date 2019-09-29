import bpy
from . import quick_toon
from bpy.props import FloatVectorProperty, IntProperty

bl_info = {
    "name": "QuickToon",
    "author": "Pratik Deolasi",
    "description": "An addon that quickly generates toon shaders",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Material"
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
        default=2,
        soft_min=2,
        soft_max=10
    )

    def execute(self, context):
        quick_toon.add_shader(material=context.material, start_color=self.start_shade, end_color=self.end_shade, shades=self.shades)
        return {'FINISHED'}


class ToonMenu(bpy.types.Panel):
    bl_idname = "TOON_SHADER_generate"
    bl_label = "Generate toon shader"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.generateshader", text="generate shader")


classes = (GenerateShaderOperator, ToonMenu)

def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ is "__main__":
    register()
