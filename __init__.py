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
    bl_idname = "object.generate_shader"
    bl_label = "Generate shader"

    start_shade: FloatVectorProperty(
        name="Color 1",
        description="The RGBA values of the starting color",
        size=4,
        default=(1, 1, 1, 1),
        subtype='COLOR',
        soft_max=1.0,
        soft_min=0.0
    )

    end_shade: FloatVectorProperty(
        name="Color 2",
        description="the RGBA values of the ending color",
        size=4,
        default=(0, 0, 0, 1),
        subtype='COLOR',
        soft_max=1.0,
        soft_min=0.0
    )

    shades: IntProperty(
        name="Number of shades",
        description="the number of shades in the shader",
        default=2,
        soft_min=2,
        soft_max=10
    )

    def execute(self, context):
        quick_toon.add_shader(material=context.material, start_color=context.object.start_shade, end_color=context.object.end_shade, shades=context.object.shades)
        return {'FINISHED'}


class ToonMenu(bpy.types.Panel):
    bl_idname = "TOON_SHADER_PT_generate"
    bl_label = "Generate toon shader"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        layout.row().label(text="Base colors:")
        layout.row().prop(context.object, "start_shade")
        layout.row().prop(context.object, "end_shade")
        layout.row().prop(context.object, "shades")
        layout.row().operator("object.generate_shader", text="Generate shader")


classes = (GenerateShaderOperator, ToonMenu)

def register():
    #the following properties are for testing purposes
    bpy.types.Object.start_shade = FloatVectorProperty(
        name="start_shade",
        description="The RGBA values of the starting color",
        size=4,
        subtype='COLOR',
        soft_max=1.0,
        soft_min=0.0
    )

    bpy.types.Object.end_shade = FloatVectorProperty(
        name="end_shade",
        description="the RGBA values of the ending color",
        size=4,
        subtype='COLOR',
        soft_max=1.0,
        soft_min=0.0
    )

    bpy.types.Object.shades = IntProperty(
        name="shades",
        description="the number of shades in the shader",
        default=2,
        soft_min=2,
        soft_max=10
    )
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ is "__main__":
    register()
