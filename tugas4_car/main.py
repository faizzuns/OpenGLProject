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
import glm

import sys
import json
import random
import threading
import msvcrt
from copy import deepcopy
from time import sleep
from math import cos, sin, radians
from time import time

vertices = []
colors = []
indices = []

width = 1200
height = 1000

vao = None          # vertex array object
buffers = None      # 3D vbo
shader = None

fps = 24
theta = 20          # in degrees

# setting up camera vectors
camera_position = glm.vec3(0.0, 0.0, 3.0)
camera_target = glm.vec3(0.0, 0.0, 0.0)
camera_direction = glm.normalize(camera_position - camera_target)   # actually negative of actual camera direction
up_vector = glm.vec3(0.0, 1.0, 0.0)
camera_right = glm.normalize(glm.cross(up_vector, camera_direction))
camera_up = glm.cross(camera_direction, camera_right)


class Shader(object):

    def initShader(self, vertex_shader_source, fragment_shader_source):
        # vertex shader
        self.vs = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(self.vs, [vertex_shader_source])
        glCompileShader(self.vs)
        printOpenGLError()
        # fragment shader
        self.fs = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(self.fs, [fragment_shader_source])
        glCompileShader(self.fs)
        printOpenGLError()
        # shader program
        self.program = glCreateProgram()
        glAttachShader(self.program, self.vs)
        glAttachShader(self.program, self.fs)
        printOpenGLError()
        glLinkProgram(self.program)
        printOpenGLError()
        self.uniform_loc = glGetUniformLocation(self.program, 'mvp_matrix')

    def begin(self):
        if glUseProgram(self.program):
            printOpenGLError()

    def use(self):
        # glUseProgram(0)
        glUseProgram(self.program)

    # def setMat4(self, mat):
    #     glUniformMatrix4fv(self.uniform_loc, 1, GL_FALSE, mat)


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
    global vertices
    vbo = glGenBuffers(3)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER,
                 len(vertices)*4,  # byte size
                 (ctypes.c_float*len(vertices))(*vertices),
                 GL_STREAM_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
    glBufferData(GL_ARRAY_BUFFER,
                 len(colors)*4,  # byte size
                 (ctypes.c_float*len(colors))(*colors),
                 GL_STREAM_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vbo[2])
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                 len(indices)*4,  # byte size
                 (ctypes.c_uint*len(indices))(*indices),
                 GL_STREAM_DRAW)
    return vbo


def draw_vbo():
    global buffers
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glVertexPointer(3, GL_FLOAT, 0, None)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glColorPointer(3, GL_FLOAT, 0, None)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2])
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    # glDisableClientState(GL_COLOR_ARRAY)
    # glDisableClientState(GL_VERTEX_ARRAY)


def reshape_func(w, h):
    resizeWindow(w, h == 0 and 1 or h)


def disp_func():
    draw()
    glutSwapBuffers()


def draw():
    # global yaw, pitch
    # clear
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -2.0)
    draw_pentagon()


def draw_pentagon():
    global shader, buffers, vao
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    if shader == None:
        shader = Shader()
        shader.initShader(
        '''
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
        # print(shader)
        buffers = create_vbo()

    shader.begin()
    shader.use()
    glBindVertexArray(vao)
    draw_vbo()
    rotateObj()
    # glBindVertexArray(0)


def add_point(x, y, z, color, i):
    vertices.append(x)
    vertices.append(y)
    vertices.append(z)

    colors.append(color[0])
    colors.append(color[1])
    colors.append(color[2])

    indices.append(i)


def load_data():
    with open("input_unicorn.json") as json_file:
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


def rotateObj():
    global shader
    view = glm.mat4(1.0)      # make sure to initialize matrix to identity matrix first
    radius = 10.0
    camX = sin(time()) * radius
    camZ = cos(time()) * radius
    view = glm.lookAt(glm.vec3(camX, 0.0, camZ), glm.vec3(0.0, 0.0, 0.0), glm.vec3(0.0, 1.0, 0.0))
    # print(shader)
    # shader.setMat4(view)


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


# def cameraTransform():
#     global shader


def rotate3d():
    global vertices, fps
    local_vertices = [0 for _ in range(len(vertices))]
    rad = radians(theta)
    m = [
        [cos(rad), 0, sin(rad)],
        [0, 1, 0],
        [-sin(rad), 0, cos(rad)]
    ]
    for i in range(0, len(vertices), 3):
        local_vertices[i], local_vertices[i + 1], local_vertices[i+2] = dot(m, vertices[i:i+3])
    vertices = deepcopy(local_vertices)
    glutPostRedisplay()
    # sleep(1//fps)
    # updateVBOData()
    # sleep(1//fps)


if __name__ == "__main__":
    load_data()

    # threading the OpenGL
    t = threading.Thread(target=main_opengl)
    t.daemon = True
    t.start()

    # rotate3d()

    # reading key presses (only works in Windows)
    while True:
        key = msvcrt.getch().decode("utf-8")
        if (key == 'a' or key == 'A'):      # rotate left
            print('you pressed left')
        elif (key == 'd' or key == 'D'):    # rotate right
            print('you pressed right')
        elif (key == 'q' or key == 'Q'):    # quit program
            print('Good bye!', end='')
            break
        rotate3d()
