'''
Reference:
https://gist.github.com/ousttrue/c4ae334fc1505cdf4cd7
https://en.wikipedia.org/wiki/Rotation_matrix#Exponential_map
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from numpy import cross, eye, dot
from scipy.linalg import expm, norm

import sys
import json
import random
import threading
import msvcrt

vertices = []
colors = []
indices = []

width = 1300
height = 1050

buffers = None
shader = None

# axis = [1, 0, 0]
# theta = 0.5


class Shader(object):

    def initShader(self, vertex_shader_source, fragment_shader_source):
        # create program
        self.program = glCreateProgram()
        printOpenGLError()
        # vertex shader
        self.vs = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(self.vs, [vertex_shader_source])
        glCompileShader(self.vs)
        glAttachShader(self.program, self.vs)
        printOpenGLError()
        # fragment shader
        self.fs = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(self.fs, [fragment_shader_source])
        glCompileShader(self.fs)
        glAttachShader(self.program, self.fs)
        printOpenGLError()

        glLinkProgram(self.program)
        printOpenGLError()

    def begin(self):
        if glUseProgram(self.program):
            printOpenGLError()

    def end(self):
        glUseProgram(0)


def initialize():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)


def resizeWindow(Width, Height):
    # viewport
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)


def printOpenGLError():
    err = glGetError()
    if (err != GL_NO_ERROR):
        print('GLERROR: ', gluErrorString(err))
        # sys.exit()


def create_vbo():
    buffers = glGenBuffers(3)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glBufferData(GL_ARRAY_BUFFER,
                 len(vertices)*4,  # byte size
                 (ctypes.c_float*len(vertices))(*vertices),
                 GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glBufferData(GL_ARRAY_BUFFER,
                 len(colors)*4,  # byte size
                 (ctypes.c_float*len(colors))(*colors),
                 GL_STATIC_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2])
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 len(indices)*4,  # byte size
                 (ctypes.c_uint*len(indices))(*indices),
                 GL_STATIC_DRAW)
    return buffers


def draw_vbo():
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glVertexPointer(3, GL_FLOAT, 0, None)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glColorPointer(3, GL_FLOAT, 0, None)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2])
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)


def reshape_func(w, h):
    resizeWindow(w, h == 0 and 1 or h)


def disp_func():
    draw()
    glutSwapBuffers()


def draw():
    global yaw, pitch
    # clear
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -2.0)

    draw_pentagon()

    glFlush()


def draw_pentagon():
    global shader, buffers
    if shader == None:
        shader = Shader()
        shader.initShader('''
            void main()
            {
                gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                gl_FrontColor = gl_Color;
            }
        ''',
                          '''
            void main()
            {
                gl_FragColor = gl_Color;
            }
        ''')
        buffers = create_vbo()

    shader.begin()
    draw_vbo()
    shader.end()


def add_point(x, y, z, color, i):
    vertices.append(x)
    vertices.append(y)
    vertices.append(z)

    colors.append(color[0])
    colors.append(color[1])
    colors.append(color[2])

    indices.append(i)


def load_data():
    with open("input.json") as json_file:
        data = json.load(json_file)
        i = 0

        for key, value in data.items():
            for key, points in value.items():
                x = float(points[0])
                y = float(points[1])

                width_control = width / 2
                height_control = height / 2

                x = (x - width_control) / (width_control + 250)
                y = (height_control - y) / (height_control + 250)

                point_color = [random.random(), random.random(),
                               random.random()]

                add_point(x, y, 0.0, point_color, i)
                i = i + 1


def main_opengl():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow("03. Car Display")
    glutDisplayFunc(disp_func)
    glutIdleFunc(disp_func)
    glutReshapeFunc(reshape_func)
    initialize()
    glutMainLoop()


# def M(axis, theta):
#     global vertices
#     M0 = expm(cross(eye(3), axis/norm(axis)*theta))
#     print(dot(M0, vertices))
#     # theta += 0.5


if __name__ == "__main__":
    load_data()

    # threading the OpenGL
    t = threading.Thread(target=main_opengl)
    t.daemon = True
    t.start()

    # # 3d rotation
    # M(axis, theta)

    # reading key presses (only works in Windows)
    while True:
        key = msvcrt.getch().decode("utf-8")
        if (key == 'a' or key == 'A'):      # rotate left
            print('you pressed left')
        elif (key == 'd' or key == 'D'):    # rotate right
            print('you pressed right')
        elif (key == 'q' or key == 'Q'):    # quit program
            print('Good bye!')
            break
