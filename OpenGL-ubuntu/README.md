# OpenGL for Ubuntu

Tested in Ubuntu 17.04

## Install Dependencies

### GLFW

1. Download GLFW **source package** from [here](https://www.glfw.org/download.html)

2. Go to **glfw-3.x.x** directory

3. `cmake -G "Unix Makefiles"`

4. Try the one of the following. If one has worked, proceed to step 5

`sudo apt-get build-dep glfw`

or 

`sudo apt-get build-dep glfw3`

or

`sudo apt-get install cmake xorg-dev libglu1-mesa-dev`

5. `make` (may require `sudo`)

6. `make install` (may require `sudo`)

### GLAD

1. `python install glad`

## How to run

1. Go to the directory of where `main.cpp` is.

2. `make`

3. A window should be opening