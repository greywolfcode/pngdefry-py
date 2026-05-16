# pngdefrypy
Python wrapper for pngdefry CgBI to PNG converter

## Usage

### Building

1. `git clone https://github.com/greywolfcode/pngdefrypy --recursive`
2. Build pngdefry (`lib/pngdefry`) as library.
3. Place the compiled library into `src/pngdefry`

### Command Line 

pngdefrypy can be used as a command line application.

```
pngdefry.py [file(s)] [args]
    -s    append suffix to output file name
    -o    write output file(s) to path
    -a    do NOT de-multiply alpha
    -l    list all chunks
    -v    verbose processing
    -i    max IDAT chunk size in bytes (minimum: 1024; default: 524288)
    -p    process all files, not just -iphone ones (for debugging purposed only)
    -d    very verbose processing (for debugging purposes only)
    -C    ignore bad CRC32 (recommended: do NOT use this, as a bad CRC32 may indicate a deliberately damaged file)
```

### Importing

`import pngdefry`

## API

### init()

Initalises pngdefrypy. Must be run before any other pngdefrypy functions.

`pngdefry.init()`

### set_flag(flag, value)

Allows locking a flag to a certain value, either True or False.

Flag options:
```
s   append suffix to output file name
a   do NOT de-multiply alpha
l   list all chunks
v   verbose processing
p   process all files, not just -iphone ones (for debugging purposed only)
d   very verbose processing (for debugging purposes only)
C   ignore bad CRC32 (recommended: do NOT use this, as a bad CRC32 may indicate a deliberately damaged file)
```
The default is False for all options.

`pngdefry.set_flag(-a, True)`

### convert(file, s=None, o=None, a=None, l=None, v=None, i=None, p=None, d=None, C=None)

Converts a given file or list of files. Any flags not defined will use defaults.

Args:
```
file (str|Path):     Path to the file(s)
s (str|suffix):      append suffix to output file name
o (str|path):        write output file(s) to path
a (bool):            do NOT de-multiply alpha
l (bool):            list all chunks
v (bool):            verbose processing
i (int):             max IDAT chunk size in bytes (minimum: 1024)
p (bool):            process all files, not just -iphone ones (for debugging purposed only)
d (bool):            very verbose processing (for debugging purposes only)
C (bool):            ignore bad CRC32 (recommended: do NOT use this, as a bad CRC32 may indicate a deliberately damaged file)
```

