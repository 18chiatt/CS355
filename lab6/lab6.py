import sys
import math
def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()


 
def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()
	
def drawTire():
	glLineWidth(2.5)
	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-1, .5, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, .5, .5)
	#Back Side
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, .5, -.5)
	#Connectors
	glVertex3f(-1, .5, .5)
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, -.5)
	glEnd()

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
MILISECONDS = 30

class State: #Track state so we can switch perspective, move to and from origin, etc...
    x = 0
    y = 0
    z = 0
    horizontalRotation = 0
    perspective = True
    time = 0.0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def houseWithOffset(xOffset, yOffset, zOffset, yRotation):
    glPushMatrix()
    glTranslated(xOffset,yOffset,zOffset)
    glRotated(yRotation,0,1,0)
    drawHouse()
    glPopMatrix()

def drawWheel(x,z):
    glPushMatrix()
    glTranslated(x,0,z)
    rotationAngle = -State.time/10.0
    glRotated(rotationAngle,0,0,1)
    drawTire()
    glPopMatrix()

def drawCarFromTime():
    time = State.time
    glPushMatrix()
    glTranslated(time/500.0, 1.0,0.0)
    drawCar()
    offset = 2.5
    for x,z in [(-offset,-offset), (offset,-offset), (-offset,offset), (offset,offset)]:
        drawWheel(x,z)
    glPopMatrix()


houses = [(0,0,-10,0), (15,0,-10,0), (-15,0,-10,0), (-30,0,5,90), (0,0,30,180), (15,0,30,180), (-15,0,30,180), ]

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    for house in houses:
        houseWithOffset(house[0],house[1],house[2],house[3])
    drawCarFromTime()
    glFlush()


def timeTracker(requiredArg):
    glutPostRedisplay()
    State.time += MILISECONDS
    glutTimerFunc(MILISECONDS, timeTracker, None)
    


def keyboard(key, x, y):
    
    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        # find x,z components of the move based on the horizontal rotation
        x,z = math.sin(math.radians(-State.horizontalRotation)), math.cos(math.radians(-State.horizontalRotation))
        glTranslated(x,0,z) 
        State.x, State.z = State.x + x, State.z + z
    if key == b's':
        # Moving backwards is just moving forwards but if you were facing the other direction
        x,z = math.sin(math.radians(-State.horizontalRotation + 180)), math.cos(math.radians(-State.horizontalRotation + 180))
        glTranslated(x,0,z) 
        State.x, State.z = State.x + x, State.z + z
    if key == b'a':
        # Moving left is just moving forward when you are facing 90 degrees more left
        x,z = math.sin(math.radians(-State.horizontalRotation + 90)), math.cos(math.radians(-State.horizontalRotation + 90))
        glTranslated(x,0,z) 
        State.x, State.z = State.x + x, State.z + z
    if key == b'd':
        x,z = math.sin(math.radians(-State.horizontalRotation - 90)), math.cos(math.radians(-State.horizontalRotation - 90))
        glTranslated(x,0,z) 
        State.x, State.z = State.x + x, State.z + z
    if key == b'r':
        glTranslated(0,-1,0) # Cabbit 
    if key == b'f':
        glTranslated(0,1,0)
    if key == b'h':
        State.time = 0
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(90,1,1, 50)
        glTranslated(0,-5,-20)
        State.x, State.y, State.z, State.horizontalRotation = 0,-5,-20,0
    if key == b'q':
        # Move camera to origin first so the rotation will happen around
        # its axis rather than 0,0,0 ... Then move it back
        glTranslated(-State.x,-State.y,-State.z)
        glRotated(-State.horizontalRotation,0,1,0)
        State.horizontalRotation -= 1
        glRotated(State.horizontalRotation,0,1,0)
        glTranslated(State.x,State.y,State.z)


    if key == b'e':
        glTranslated(-State.x,-State.y,-State.z)
        glRotated(-State.horizontalRotation,0,1,0)
        State.horizontalRotation += 1
        glRotated(State.horizontalRotation,0,1,0)
        glTranslated(State.x,State.y,State.z)

    
    if key == b'o':
        if not State.perspective:
            return
        State.perspective = False
        glLoadIdentity()
        #Define clipping box
        glOrtho(-5.0,5.0,-5.0,5.0,-5.0,1000.0)
        #Move ortho projection into right spot
        glRotated(State.horizontalRotation,0,1,0)
        glTranslatef(State.x,State.y,State.z)

    if key == b'p':
        if State.perspective:
            return
        State.perspective = True
        glLoadIdentity()
        gluPerspective(90,1,1, 50)
        # Load perspective and move into correct position
        glRotated(State.horizontalRotation,0,1,0)
        glTranslatef(State.x, State.y,State.z)

  
    glutPostRedisplay()


glutInit(sys.argv)
glutTimerFunc(10, timeTracker, None)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
gluPerspective(90,1,0, 50)
glTranslatef(0,-5,-20)
State.x, State.y, State.z = 0,-5,-20
# good default start so you can see the house
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
