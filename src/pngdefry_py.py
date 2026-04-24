import ctypes
import platform
from pathlib import Path

# variable to store library in
_pngdefry_lib = None 
_initalised = False

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
    global _initalised

    # load required library
    if platform.system == "Windows":
        _pngdefry_lib = ctypes.CDLL("pngdefry.dll")
    elif platform.system == "Linux":
        _pngdefry_lib = ctypes.CDLL("pngdefry.so")
    else:
        raise OSError("No library is supported for your OS")

    # specify arg types
    _pngdefry_lib.main.argtypes = (c_int, POINTER(c_char_p))

    _initalised = True

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

def _get_file_list(files):
    #s ingle file in a string
    if isinstance(files, str):
        return [files]
    elif isinstance(files, list):
        pass
    # not a valid path type!
    elif not isinstance(files, tuple) and not isinstance(files, set) and not isinstance(files, list):
        raise TypeError(str(files) + " of type " + type(files) + " is not a valid type for file path")
    
    # iterate through what files are stored in
    paths = []
    for file in files:
        if isinstance(file, str):
            paths.append(file)
        elif isinstance(file, Path):
            paths.append(str(file))
        # not a valid path type!
        else:
            raise TypeError(str(file) + " of type " + type(file) +  "is not a valid type for file path")
    return paths

def _enocde_utf_8(string):
    return string.encode("utf-8)")

def convert(file, s=None, o=None, a=None, l=None, v=None, i=None, p=None, d=None, C=None):
    """
	Removes -iphone specific data chunk, reverses colors from BGRA to RGBA, and de-multiplies alpha
	
    Args:
        file (str/Path) Path to the file(s)
		s (suffix)      append suffix to output file name
		o (path)        write output file(s) to path
		a (bool)        do NOT de-multiply alpha
		l (bool)        list all chunks
		v (bool)        verbose processing
		i (value)       max IDAT chunk size in bytes (minimum: 1024)
		p (bool)        process all files, not just -iphone ones (for debugging purposed only)
		d (bool)        very verbose processing (for debugging purposes only)
		C (bool)        ignore bad CRC32 (recommended: do NOT use this, as a bad CRC32 may indicate a deliberately damaged file)

    Note: without s or o, NO output will be created;
    """

    if not _initalised:
        raise RuntimeError("pngdefry was not initalised")

    args = []

    # add args to list to args
    # fall back to default flags if None

    if s != None:
        args.append("-s")
        args.append(s)
    if o != None:
        args.append("-o")
        args.append(o)
    if a == None:
        if _dont_multiply_alpha:
            args.append("-a")
    elif a:
        args.append("-a")
    if l == None:
        if _list_all_chunks:
            args.append("-l")
    elif l:
        args.append("-l")
    if v == None:
        if _verbose:
            args.append("-v")
    elif v:
        args.append("-v")
    if i != None:
        args.append("-i")
        args.append(i)
    if p == None:
        if _process_all_files:
            args.append("-p")
    elif p:
        args.append("-p")
    if d == None:
        if _very_verbose:
            args.append("-d")
    elif d:
        args.append("-d")
    if C == None:
        if _ignore_bad_CRC32:
            args.append("-C")
    elif C:
        args.append("-C")
    
    #files attach last
    file_paths = _get_file_list(file)
    args.extend(file_paths)

    argc = len(args)

    # convert args to array useable by C
    byte_args = list(map(_enocde_utf_8, args))
    argv = (c_char_p * argc)(*byte_args)

    _pngdefry_lib.main(argc, argv)