#include "GL/gl.h"
#include "GL/freeglut.h"
#include <math.h>


void displayPentagon()
{
    int v;
    float pent[6][2];

    // float ang, da = 6.2832 / 5.0;

    // Compute vertex coordinates.

    // for (v = 0; v < 5; v++)  {
    //     ang = v * da;
    //     pent[v][0] = cos (ang);
    //     pent[v][1] = sin (ang);
    // }

    pent[0][0] = 0.25;
    pent[0][1] = 0;

    pent[1][0] = 0;
    pent[1][1] = 0.4;

    pent[2][0] = 0.5;
    pent[2][1] = 0.8;

    pent[3][0] = 1;
    pent[3][1] = 0.4;

    pent[4][0] = 0.75;
    pent[4][1] = 0;

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.5, 1.0, 0.0);
    glBegin (GL_POLYGON);
    for (v = 0; v < 5; v++) {
        glVertex2fv(pent[v]);
    }
    glEnd();
    glFlush();
}

void displayMe(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_POLYGON);
        glVertex3f(0.5, 0.0, 0.5);
        glVertex3f(0.5, 0.0, 0.0);
        glVertex3f(0.0, 0.5, 0.0);
        glVertex3f(0.0, 0.0, 0.5);
    glEnd();
    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(0,0);
    glutCreateWindow("Pentagon Asoi");
    glutDisplayFunc(displayPentagon);
    glutMainLoop();    
    return 0;
}