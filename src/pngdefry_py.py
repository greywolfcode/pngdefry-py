import ctypes
import platform

# variable to store library in
_pngdefry_lib = None 

# arguments to pass to conversion 
_suffix = False               # -s
_dont_multiply_alpha = False  # -a
_list_all_chunks = False      # -l
_verbose = False              # -v
_process_all_files = False    # -p
_very_verbose = False         # -d
_ignore_bad_CRC32 - False     # -C

def init():
    """
    Initalises pngdefry-py and load pngdefry library
    """
    global _pngdefry_lib

    # load required library
    if platform.system == "Windows":
        _pngdefry_lib = ctypes.CDLL("pngdefry.dll")
    elif platform.system == "Linux":
        _pngdefry_lib = ctypes.CDLL("pngdefry.so")
    else:
        raise OSError("No library is supported for your OS")

def set_flag(flag, value):
    """
    Sets a specific flag for use in conversion

    Args: 
        flag (string): the flag to set
        value (boolean): the value to set the flag to

    Flag Options:
    	s         append suffix to output file name
		a         do NOT de-multiply alpha
		l         list all chunks
		v         verbose processing
		p         process all files, not just -iphone ones (for debugging purposed only)
		d         very verbose processing (for debugging purposes only)
	    C         ignore bad CRC32 (recommended: do NOT use this, as a bad CRC32 may indicate a deliberately damaged file)
    """

    global _suffix
    global _dont_multiply_alpha
    global _list_all_chunks
    global _verbose
    global _process_all_files
    global _very_verbose
    global _ignore_bad_CRC32

    match value:
        case "s":
            _suffix = value
        case "a":
            _dont_multiply_alpha = value
        case "l":
            _list_all_chunks = value
        case "v":
            _verbose = value
        case "p":
            _process_all_files = value
        case "d":
            _very_verbose = value
        case "C":
            _ignore_bad_CRC32 = value
