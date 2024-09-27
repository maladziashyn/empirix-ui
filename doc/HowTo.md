# HOW TO

## Windows

### PyGObject installation guide

See [wingtk/gvsbuild](https://github.com/wingtk/gvsbuild?tab=readme-ov-file) section "Install GTK Only":

- copy and unzip the latest release
- add environmental variables: Path, LIB, INCLUDE
- run "pip install --force-reinstall ..." in the project's venv

### Frozen binaries

No additional installations needed.

## Linux

### Frozen binaries

To run Nuitka, additionally install:

`$ sudo apt install patchelf`

`$ sudo apt install ccache`
