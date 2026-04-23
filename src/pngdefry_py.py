import ctypes
import platform

_pngdefry_lib = None 

def init():
    global _pngdefry_lib

    #load required library
    if platform.system == "Windows":
        _pngdefry_lib = ctypes.CDLL("pngdefry.dll")
    elif platform.system == "Linux":
        _pngdefry_lib = ctypes.CDLL("pngdefry.so")
    else:
        raise OSError("No library is supported for your OS")