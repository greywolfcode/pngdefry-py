from pathlib import Path

import pngdefrypy

file = input("\nEnter path to CgBI file: ")
# strip off extra quotes if they exist
if (file[0] == '"' and file[-1] == '"'):
    file = file[1:-1]

# ____test not initalising pngdefry_py____

print("\nTesting conversion before initalisation:\n")
try:
    pngdefrypy.convert(file)
except(RuntimeError):
    print("Uninitalised Error succesfully thrown")

pngdefrypy.init()


# ____test each option_____
print("\nTest normal:\n")
pngdefrypy.convert(file)

print("\nTest -s:\n")
pngdefrypy.convert(file, s=".png")

print("\nTest -o:\n")
# need to create directory; pngdefry won't
Path("image_output").mkdir(exist_ok=True)
pngdpngdefrypyefry.convert(file, o="image_output")

print("\nTest -a:\n")
pngdefrypy.convert(file, a=True)

print("\nTest -l:\n")
pngdefrypy.convert(file, l=True)

print("\nTest -v:\n")
pngdefrypy.convert(file, v=True)

print("\nTest -i:\n")
pngdefrypy.convert(file, i=1024)

print("\nTest -p:\n")
pngdefrypy.convert(file, p=True)

print("\nTest -d:\n")
pngdefrypy.convert(file, d=True)

print("\nTest -C:\n")
pngdefrypy.convert(file, C=True)

# ____test setting default flags____
# No need to test them all, as setting logic is the same for all 
# default flags, and the flags were tested above
print("\nTest setting default flags:\n")

print("Turned on -f\n")
pngdefrypy.set_flag("v", True)
pngdefrypy.convert(file)

print("\nTurned off -f\n")
pngdefrypy.set_flag("v", False)
pngdefrypy.convert(file)


print("\nTurned on -d\n")
pngdefrypy.set_flag("d", True)
pngdefrypy.convert(file)