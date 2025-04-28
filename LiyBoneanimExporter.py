import bpy
import bmesh
import os
import math

C = bpy.context

filename = C.object.name + "anim"
liyaname = filename + ".liya"
file = open(os.environ['HOME'] + "/" + liyaname, "w")

framecount = 55

print("export")

bones = C.object.data.bones
posebones = C.object.pose.bones

bpy.ops.screen.frame_jump(end=False)

file.write(str(len(bones) * 9) + "\n" + str(framecount) + "\n")

print(str(len(bones) * 9) + "prims")

boneIndecies = []
boneIndeciesIdx = []
for b in range(len(bones)):
    bonename = []
    for n in range(len(bones[b].name)): 
        if (bones[b].name[n] == ","):
            break
        bonename.append(bones[b].name[n])
    bonename = int(''.join(bonename))
    boneIndecies.append(bonename)
    boneIndeciesIdx.append(b)

while(True): # sort bone indeciesidx
    sortedYet = 1
    for i in range(len(boneIndecies)-1):
        if boneIndecies[i] > boneIndecies[i+1]:
            sortedYet = 0
            b = boneIndecies[i]
            boneIndecies[i] = boneIndecies[i+1]
            boneIndecies[i+1] = b
            b = boneIndeciesIdx[i]
            boneIndeciesIdx[i] = boneIndeciesIdx[i+1]
            boneIndeciesIdx[i+1] = b
    if(sortedYet == 1):
        break
    
bonePoseIndecies = []
bonePoseIndeciesIdx = []
for b in range(len(posebones)):
    bonename = []
    for n in range(len(posebones[b].name)): 
        if (posebones[b].name[n] == ","):
            break
        bonename.append(posebones[b].name[n])
    bonename = int(''.join(bonename))
    bonePoseIndecies.append(bonename)
    bonePoseIndeciesIdx.append(b)
    
while(True): # sort bonepose indeciesidx
    sortedYet = 1
    for i in range(len(bonePoseIndecies)-1):
        if bonePoseIndecies[i] > bonePoseIndecies[i+1]:
            sortedYet = 0
            b = bonePoseIndecies[i]
            bonePoseIndecies[i] = bonePoseIndecies[i+1]
            bonePoseIndecies[i+1] = b
            b = bonePoseIndeciesIdx[i]
            bonePoseIndeciesIdx[i] = bonePoseIndeciesIdx[i+1]
            bonePoseIndeciesIdx[i+1] = b
    if(sortedYet == 1):
        break
    
boneDefaultPos = []
boneDefaultRot = []
    
for b in range(len(bones)):
    p = bones[b].matrix_local.to_translation()
    v = bones[b].matrix_local.to_quaternion()
    
    boneDefaultPos.append(p)
    boneDefaultRot.append(v)
    
print(boneDefaultRot)
    
for f in range(framecount):
    for b in range(len(bones)):        
        mtxpos = posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        mtxpos -= boneDefaultPos[boneIndeciesIdx[b]]
        s = posebones[bonePoseIndeciesIdx[b]].matrix.to_scale()
        drot = posebones[bonePoseIndeciesIdx[b]].matrix.to_quaternion() @ boneDefaultRot[boneIndeciesIdx[b]].inverted()
        mtxpos = mtxpos - posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        mtxpos = drot @ mtxpos
        mtxpos = mtxpos + posebones[bonePoseIndeciesIdx[b]].matrix.to_translation()
        p1 = mtxpos[0]
        p2 = mtxpos[1]
        p3 = mtxpos[2]
        
        drot = drot.to_euler()
        
        lala1 = f"{p1:.4f}"
        lala2 = f"{p2:.4f}"
        lala3 = f"{p3:.4f}"
        out1 = lala1 + " " + lala2 + " " + lala3 + " "
        file.write(out1)
        
        lala1 = f"{drot.x:.4f}"
        lala2 = f"{drot.y:.4f}"
        lala3 = f"{drot.z:.4f}"
        out1 = lala1 + " " + lala2 + " " + lala3 + " "
        file.write(out1)
        
        lala1 = f"{s.x:.4f}"
        lala2 = f"{s.y:.4f}"
        lala3 = f"{s.z:.4f}"
        out1 = lala1 + " " + lala2 + " " + lala3 + " "
        file.write(out1)
    bpy.ops.screen.frame_offset(delta=1) 

file.close()