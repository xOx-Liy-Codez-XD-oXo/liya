import bpy
import bmesh
import os
import math

C = bpy.context
filename = C.object.name + "shapeanim"
liyaname = filename + ".liya"
file = open(os.environ['HOME'] + "/" + liyaname, "w")

framecount = 40

print("export")

bpy.ops.screen.frame_jump(end=False)

#amnt of prims per frame then the frame count
#for us, amount of shape keys exactly
file.write(str(len(C.object.data.shape_keys.key_blocks)-1) + "\n" + str(framecount) + "\n")

for f in range(framecount):
    for k in range(len(C.object.data.shape_keys.key_blocks)-1):
        lala1 = C.object.data.shape_keys.key_blocks[k+1].value
        lala2 = f"{lala1:.4f}"
        out1 = lala2 + " "
        file.write(out1)
    bpy.ops.screen.frame_offset(delta=1)

file.close()