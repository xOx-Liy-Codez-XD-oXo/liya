# LIYA
LIYA is a streaming file format for the Wii. The streamer loads an equal piece of the file every frame. LIYA can also be used as an intermediary format between Blender and further tools. 
## LIYA boneanim export script usage
The script expects that all the bones are numbered at the start with a comma following. The script will export the bone's transform offset from the origin, apt for immediately calculating a modelview matrix from the animation data with minimal processing, i.e. a skeleton in it's default pose will be exported with all zeroes for that frame. 
Open the script in a Blender text editor, set the amount of frames to export, select your armature in a 3D viewport, and click the play button in the text editor.

## LIYA file walkthrough. 
Walkthrough of this file. 
```
522
55
-0.0063 -0.0376 -0.0014 -0.0468 -0.0007 -0.1500 1.0000 1.0000 1.0000 ...
```
### `522`
The amount of floats per frame. "primcount". This specific file is a skeletal animation, for which each bone's location, rotation, and scale is stored per frame, thus the amount of bones can be deduced by dividing 522 by 9 to find 58 bones in this animation. LIYA files do not need to be skeletal animations, they can stream any data. 
### `55`
The amount of frames in this file. "framecount"
### `buncha numbers`
Lots of floating point numbers separated by spaces and ended with a line break. There will always be primcount * framecount floats here. 
