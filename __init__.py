bl_info = {
    "name": "SantarhAddOns",
    "auther": "santarh",
    "category": "User"
}

import bpy
import os

from . import bone_constraints

def register():
    bpy.utils.register_class(bone_constraints.TheOthersBoneLocationConstraints)

def unregister():
    bpy.utils.unregister_class(bone_constraints.TheOthersBoneLocationConstraints)

if __name__ == "__main__":
    register()
