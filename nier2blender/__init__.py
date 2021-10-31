bl_info = {
    "name": "Nier: Automata model importer",
    "author": "C4nf3ng",
    "version": (1, 1),
    "blender": (2, 93, 0),
    "api": 38019,
    "location": "File > Import-Export",
    "description": "Import Nier:Automata wmb model data",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}

#just for Break

import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty

class ImportNier2blender(bpy.types.Operator, ImportHelper):
    '''Load a Nier: Automata WMB File.'''
    bl_idname = "import.wmb_data"
    bl_label = "Import WMB Data"
    bl_options = {'PRESET'}
    filename_ext = ".wmb"
    filter_glob = StringProperty(default="*.wmb", options={'HIDDEN'})

    def execute(self, context):
        from nier2blender import wmb_importer
        return wmb_importer.main( self.filepath)


# Registration
classes = (ImportNier2blender,)

def menu_func_import(self, context):
    self.layout.operator(ImportNier2blender.bl_idname, text="WMB File for Nier: Automata (.wmb)")


def register():
    for cls in classes: bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    for cls in reversed(classes): bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == '__main__':
    register()