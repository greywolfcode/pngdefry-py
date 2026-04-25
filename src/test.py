import pngdefry

file = input("\nEnter path to CgBI file: ")
# strip off extra quotes if they exist
if (file[0] == '"' and file[-1] == '"'):
    file = file[1:-1]

# ____test not initalising pngdefry____

try:
    pngdefry.convert(file)
except(RuntimeError):
    print("\nUninitalised Error succesfully thrown")

pngdefry.init()


# ____test each option_____
print("\nTest normal:\n")
pngdefry.convert(file)

print("\nTest -s:\n")
pngdefry.convert(file, s=".png")

print("\nTest -o:\n")
pngdefry.convert(file, o="image_output/")

print("\nTest -a:\n")
pngdefry.convert(file, a=True)

print("\nTest -l:\n")
pngdefry.convert(file, l=True)

print("\nTest -v:\n")
pngdefry.convert(file, v=True)

print("\nTest -i:\n")
pngdefry.convert(file, i=1024)

print("\nTest -p:\n")
pngdefry.convert(file, p=True)

print("\nTest -d:\n")
pngdefry.convert(file, d=True)

print("\nTest -C:\n")
pngdefry.convert(file, C=True)

# ____test setting default flags____
# No need to test them all, as setting logic is the same for all 
# default flags, and the flags were tested above
print("\nTest setting default flags:\n")

print("Turned on -f\n")
pngdefry.set_flag("v", True)
pngdefry.convert(file)

print("\nTurned off -f\n")
pngdefry.set_flag("v", False)
pngdefry.convert(file)


print("\nTurned on -d\n")
pngdefry.set_flag("d", True)
pngdefry.convert(file)