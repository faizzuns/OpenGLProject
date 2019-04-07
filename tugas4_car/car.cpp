#include <math.h>
#include <GL/glut.h>


float transZ=50;      
float rotateA=0;         

float rotateAspeed=0.0;

void car (float dimX, float dimY, float dimZ)
{
   glMatrixMode(GL_MODELVIEW);
   glPushMatrix();

    glTranslatef(0,dimY/2,0);
    glScalef(dimX/2, dimY/2, dimZ/2);

    glBegin(GL_QUADS);                /* OBJECT MODULE*/

      /* top of cube*/
      //************************FRONT BODY****************************************
      glColor3f(0,0,0);
      glVertex3f( 0.2, 0.4,0.6);
      glVertex3f(0.6, 0.5,0.6);
      glVertex3f(0.6, 0.5,0.2);
      glVertex3f( 0.2,0.4,0.2);

      /* bottom of cube*/
      glVertex3f( 0.2,0.4,0.6);
      glVertex3f(0.6,0.2,0.6);
      glVertex3f(0.6,0.2,0.2);
      glVertex3f( 0.2,0.2,0.2);

      /* front of cube*/
      glVertex3f( 0.2,0.2,0.6);
      glVertex3f(0.2, 0.4,0.6);
      glVertex3f(0.2,0.4,0.2);
      glVertex3f( 0.2,0.2,0.2);

      /* back of cube.*/
      glVertex3f(0.6,0.2,0.6);
      glVertex3f(0.6,0.5,0.6);
      glVertex3f(0.6,0.5,0.2);
      glVertex3f( 0.6,0.2,0.2);

      /* left of cube*/
      glVertex3f(0.2,0.2,0.6);
      glVertex3f(0.6,0.2,0.6);
      glVertex3f(0.6,0.5,0.6);
      glVertex3f(0.2,0.4,0.6);

      /* Right of cube */
      glVertex3f(0.2,0.2,0.2);
      glVertex3f( 0.6,0.2,0.2);
      glVertex3f( 0.6,0.5,0.2);
      glVertex3f( 0.2,0.4,0.2);
    //****************************************************************************
      glVertex3f(0.7,0.65,0.6);
      glVertex3f(0.7,0.65,0.2);
      glVertex3f(1.7,0.65,0.2);        //top cover
      glVertex3f(1.7,0.65,0.6);
    //***************************back guard******************************
      glColor3f(0,0,0);            /* Set The Color To Blue*/
      glVertex3f( 1.8, 0.5,0.6);
      glVertex3f(1.8, 0.5,0.2);
      glVertex3f(2.1, 0.4, 0.2);
      glVertex3f(2.1,0.4,0.6);

      /* bottom of cube*/
      glVertex3f( 2.1,0.2,0.6);
      glVertex3f(2.1,0.2,0.2);
      glVertex3f(1.8,0.2,0.6);
      glVertex3f( 1.8,0.2,0.6);

      /* back of cube.*/
      glVertex3f(2.1,0.4,0.6);
      glVertex3f(2.1,0.4,0.2);
      glVertex3f(2.1,0.2,0.2);
      glVertex3f(2.1,0.2,0.6);

      /* left of cube*/
      glVertex3f(1.8,0.2,0.2);
      glVertex3f(1.8,0.5,0.2);
      glVertex3f(2.1,0.4,0.2);
      glVertex3f(2.1,0.2,0.2);

      /* Right of cube */
      glVertex3f(1.8,0.2,0.6);
      glVertex3f(1.8,0.5,0.6);
      glVertex3f(2.1,0.4,0.6);
      glVertex3f(2.1,0.2,0.6);
    //******************MIDDLE BODY************************************
      glVertex3f( 0.6, 0.5,0.6);
      glVertex3f(0.6, 0.2,0.6);
      glVertex3f(1.8, 0.2, 0.6);
      glVertex3f(1.8,0.5,0.6);

      /* bottom of cube*/
      glVertex3f( 0.6,0.2,0.6);
      glVertex3f(0.6,0.2,0.2);
      glVertex3f(1.8,0.2,0.2);
      glVertex3f( 1.8,0.2,0.6);

      /* back of cube.*/
      glVertex3f(0.6,0.5,0.2);
      glVertex3f(0.6,0.2,0.2);
      glVertex3f(1.8,0.2,0.2);
      glVertex3f(1.8,0.5,0.2);
    //*********************ENTER WINDOW**********************************
      glColor3f(0.3,0.3,0.3);
      glVertex3f( 0.77, 0.63,0.2);
      glVertex3f(0.75, 0.5,0.2);        //quad front window
      glVertex3f(1.2, 0.5, 0.2);
      glVertex3f( 1.22,0.63,0.2);

      glVertex3f(1.27,0.63,.2);
      glVertex3f(1.25,0.5,0.2);        //quad back window
      glVertex3f(1.65,0.5,0.2);
      glVertex3f(1.67,0.63,0.2);

      glColor3f(0,0,0);
      glVertex3f(0.7,0.65,0.2);
      glVertex3f(0.7,0.5,.2);       //first separation
      glVertex3f(0.75,0.5,0.2);
      glVertex3f(0.77,0.65,0.2);

      glVertex3f(1.2,0.65,0.2);
      glVertex3f(1.2,0.5,.2);       //second separation
      glVertex3f(1.25,0.5,0.2);
      glVertex3f(1.27,0.65,0.2);

      glVertex3f(1.65,0.65,0.2);
      glVertex3f(1.65,0.5,.2);     //3d separation
      glVertex3f(1.7,0.5,0.2);
      glVertex3f(1.7,0.65,0.2);

      glVertex3f( 0.75, 0.65,0.2);
      glVertex3f(0.75, 0.63,0.2);        //line strip
      glVertex3f(1.7, 0.63, 0.2);
      glVertex3f( 1.7,0.65,0.2);

      glVertex3f( 0.75, 0.65,0.6);
      glVertex3f(0.75, 0.63,0.6);        //line strip
      glVertex3f(1.7, 0.63, 0.6);
      glVertex3f( 1.7,0.65,0.6);

      glColor3f(0.3,0.3,0.3);
      glVertex3f( 0.77, 0.63,0.6);
      glVertex3f(0.75, 0.5,0.6);        //quad front window
      glVertex3f(1.2, 0.5, 0.6);
      glVertex3f( 1.22,0.63,0.6);

      glVertex3f(1.27,0.63,.6);
      glVertex3f(1.25,0.5,0.6);        //quad back window
      glVertex3f(1.65,0.5,0.6);
      glVertex3f(1.67,0.63,0.6);

      glColor3f(0,0,0);
      glVertex3f(0.7,0.65,0.6);
      glVertex3f(0.7,0.5,.6);       //first separation
      glVertex3f(0.75,0.5,0.6);
      glVertex3f(0.77,0.65,0.6);

      glVertex3f(1.2,0.65,0.6);
      glVertex3f(1.2,0.5,.6);       //second separation
      glVertex3f(1.25,0.5,0.6);
      glVertex3f(1.27,0.65,0.6);

      glVertex3f(1.65,0.65,0.6);
      glVertex3f(1.65,0.5,.6);
      glVertex3f(1.7,0.5,0.6);
      glVertex3f(1.7,0.65,0.6);

    glEnd();

  glBegin(GL_TRIANGLES);                /* start drawing the cube.*/

    /* top of cube*/
    glColor3f(0.3,0.3,0.3);
    glVertex3f( 0.6, 0.5,0.6);
    glVertex3f( 0.7,0.65,0.6);       //tri front window
    glVertex3f(0.7,0.5,0.6);

    glVertex3f( 0.6, 0.5,0.2);
    glVertex3f( 0.7,0.65,0.2);       //tri front window
    glVertex3f(0.7,0.5,0.2);

    glVertex3f( 1.7, 0.65,0.2);
    glVertex3f( 1.8,0.5,0.2);       //tri back window
    glVertex3f( 1.7,0.5,0.2);

    glVertex3f( 1.7, 0.65,0.6);
    glVertex3f( 1.8,0.5,0.6);       //tri back window
    glVertex3f(1.7,0.5,0.6);

  glEnd();

  //wheel
  glColor3f(0.7,0.7,0.7);
  glPushMatrix();
  glBegin(GL_LINE_STRIP);
    for(float theta=0;theta<360;theta=theta+40)
    {
      glVertex3f(0.6,0.2,0.62);
      glVertex3f(0.6+(0.08*(cos(((theta)*3.14)/180))),0.2+(0.08*(sin(((theta)*3.14)/180))),0.62);
    }
  glEnd();

  glBegin(GL_LINE_STRIP);
    for(float theta=0;theta<360;theta=theta+40)
    {
      glVertex3f(0.6,0.2,0.18);
      glVertex3f(0.6+(0.08*(cos(((theta)*3.14)/180))),0.2+(0.08*(sin(((theta)*3.14)/180))),0.18);
    }
  glEnd();

  glBegin(GL_LINE_STRIP);
    for(float theta=0;theta<360;theta=theta+40)
    {
      glVertex3f(1.7,0.2,0.18);
      glVertex3f(1.7+(0.08*(cos(((theta)*3.14)/180))),0.2+(0.08*(sin(((theta)*3.14)/180))),0.18);
    }
  glEnd();

  glBegin(GL_LINE_STRIP);
    for(float theta=0;theta<360;theta=theta+40)
    {
      glVertex3f(1.7,0.2,0.62);
      glVertex3f(1.7+(0.08*(cos(((theta)*3.14)/180))),0.2+(0.08*(sin(((theta)*3.14)/180))),0.62);
    }
  glEnd();

  glColor3f(255,0,0);
  glTranslatef(0.6,0.2,0.6);
  glutSolidTorus(0.025,0.07,10,25);

  glColor3f(0,255,0);
  glTranslatef(0.6,0.2,0.2);
  glutSolidTorus(0.025,0.07,10,25);

  glColor3f(0,0,255);
  glTranslatef(1.1,0,0.4);
  glutSolidTorus(0.025,0.07,10,25);

  glColor3f(0,255,255);
  glTranslatef(0,0,-0.4);
  glutSolidTorus(0.025,0.07,10,25);

  glPopMatrix();

}

void display(void)
{
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   gluLookAt(transZ*cos(rotateA),10,transZ*sin(rotateA), 0,10,0, 0,1,0);
   car(30,30,30);
   glFlush();            
   glutSwapBuffers();
}

void init (void)
{
   glClearColor(1.0, 1.0, 1.0, 1.0);
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glFrustum(-1, 1, -1, 1, 1, 1000);
   glEnable(GL_DEPTH_TEST); 
}


void keyboard(unsigned char key, int x, int y)
{
   switch (key) {
      case 27:                
         exit(0);
         break;
      case 'S':
         transZ+=1.0f;
         glutPostRedisplay();  
         break;
      case 'W':
         transZ-=1.0f;
         if (transZ<0) transZ=0;
         glutPostRedisplay();  
         break;
      case 's':
         transZ+=0.5f;
         glutPostRedisplay();  
         break;
      case 'w':
         transZ-=0.5f;
         if (transZ<0) transZ=0;
         glutPostRedisplay(); 
         break;
      case 'A':
         rotateAspeed+=0.001f;
         glutPostRedisplay();  
         break;
      case 'a':
         rotateAspeed+=0.001f;
         glutPostRedisplay();  
         break;
      case 'D':
         rotateAspeed-=0.001f;
         glutPostRedisplay();  
         break;
      case 'd':
         rotateAspeed-=0.001f;
         glutPostRedisplay();  
         break;

   }
}

void idle(void)
{
  rotateA=rotateA + rotateAspeed;
  glutPostRedisplay();    
}

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
   glutInitWindowSize (500, 500);
   glutInitWindowPosition (100, 100);
   glutCreateWindow ("Car");
   init ();

   glutDisplayFunc(display);
   glutIdleFunc(idle); 

   glutKeyboardFunc(keyboard); 
   glutMainLoop();
   return 0;
}