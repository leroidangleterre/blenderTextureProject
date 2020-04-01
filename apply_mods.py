# TODO before using this script



# Create an object with a material and a UV-texture using an image
# Duplicate the object (non-linked duplication, Shift+D)
# Make objects move (ex: rigid body tools)
# BAKE THE ANIMATION
# Create a UV-map for the first object and use "Project from view"

# Add the path to this image in this script;
# Manually create a modifier for one object, choose the UVProject modifier;
#   -> select the image and the UV-map in the modifier's parameters;
#   -> Under "Projectors: 1", choose the camera as the projector.

# Ctrl + L -> Modifiers will copy the modifier to all objects.
#   -> Set the size of the image on the modifier (Aspect X and Aspect Y) and test by copying the modifier to all cubes with Ctrl+L.

# Select the objects, then press U (Make single users), Objects & Data & Mat+tex

# Make sure the objects are named "Cube.***"

# Run script.

import bpy
print("coucou")

image=name = "C:\\Users\\arthurmanoha\\Documents\\Blender\\Kapla textures\\kaplaTex_2020\\Central_Park.jpg"
index_max = 1723


for index in range(0, index_max):
    if(index<10):
        name = "Cube.00" + str(index)
    elif(index<100):
        name = "Cube.0" + str(index)
    else:
        name = "Cube." + str(index)
    
    # Select the n-th cube
    try:
        bpy.data.objects[name].select = True
#        bpy.data.objects[name].select = False
        
                
        # Apply its modifier
        bpy.context.scene.objects.active = bpy.data.objects[name]
        bpy.ops.object.modifier_apply(modifier='UVProject', apply_as='DATA')
        print(name)
    except KeyError:
        print(name + "does not exist; ignoring.")
# end
