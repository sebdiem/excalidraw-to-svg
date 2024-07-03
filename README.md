# excalidraw-to-svg

This is a simple wrapper around [excalidraw-to-svg](https://github.com/JRJurman/excalidraw-to-svg).
Since this library requires a few system dependencies let's bundle all this into a docker image and make it an executable.
The result is not optimized at all (170Mb image + more than a second to run) but it works ¯\\\_(ツ)\_/¯

## Prerequisites

A working docker install

## Usage

```sh
python excalidraw_to_svg/main.py myfile.excalidraw
```

You can also install it via [poetry](https://python-poetry.org/) and run the `excalidraw-to-svg` executable.

```sh
poetry add git+https://github.com/sebdiem/excalidraw-to-svg
excalidraw-to-svg myfile.excalidraw
```
