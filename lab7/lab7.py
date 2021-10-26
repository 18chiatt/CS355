# Import a library of functions called 'pygame'
from numpy.core.fromnumeric import clip
import pygame
import math
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
class Line3D():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end


def makeTransformMatrix(x,y,z):
    return np.matrix([
        [1,0,0,-x],
        [0,1,0,-y],
        [0,0,1,-z],
        [0,0,0,1]
    ])

def normalize(v):
    return v / np.sqrt(np.sum(v**2))

def cross(a, b):
    c = np.cross(a,b)
    return c


def makeRotationMatrix(xRot):
    rotationMatrix = np.array([
        [math.cos(math.radians(xRot)),0,math.sin(math.radians(xRot)),0],
        [0,1,0,0],
        [-math.sin(math.radians(xRot)),0,math.cos(math.radians(xRot)),0],
        [0,0,0,1],

    ])
    return rotationMatrix

def makeZRotationMatrix(zRot):
    rads = math.radians(zRot)
    cos, sin = math.cos, math.sin
    return np.array([
        [cos(rads), -sin(rads),0,0],
        [sin(rads),cos(rads),0,0],
        [0,0,1,0],
        [0,0,0,1],
    ])

def makeProjectionClipMatrix(fov, near, far):
    far,near, fov = float(far), float(near), float(fov)
    zoom = 1.0/( math.tan(math.radians(fov/2.0)) )
    mat = np.array([
        [zoom,0,0,0],
        [0,zoom,0,0],
        [0,0,(far + near)/(far - near), (-2.0 * near * far)/(far - near)],
        [0,0,1,0],
    ])
    return mat
    




def identity():
    return np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))
    
    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire


    
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

MOVESPEED = .2
ROTSPEED = 2

# Set the height and width of the screen
size = [512, 512]
WIDTH = 512.0
HEIGHT = 512.0
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
linelist = loadHouse()

def left(s,e):
    return s[0][0] < -s[0][3] and e[0][0] < -e[0][3]

def right(s,e):
    return s[0][0] > s[0][3] and e[0][0] > e[0][3]

def bottom(s,e):
    return s[0][1] < -s[0][3] and e[0][1] < -e[0][3]

def top(s,e):
    return s[0][1] > s[0][3] and e[0][1] > e[0][3]

def near(s,e):
    return s[0][2] < -s[0][3] or e[0][2] < -e[0][3] #If either fails, fail the test

def far(s,e):
    return s[0][2] < s[0][3] and e[0][2] > e[0][3]

#Loop until the user clicks the close button.
class Camera:
    x = 0
    y = 3
    z = -5
    xrot = 0

class Car:
    startTime = 0.0

class MatrixStack:
    matricies = []
    clipAndProjection = makeProjectionClipMatrix(90,.01,100).T
    screenSpace = np.array([
        [WIDTH/2.0, 0 , WIDTH/2.0],
        [0, -HEIGHT/2.0, HEIGHT/2.0],
        [0,0,1]
    ])
    currMatrix = identity()

    @classmethod
    def getMatrix():
        return MatrixStack.currMatrix
    
    def pushMatrix():
        MatrixStack.matricies.append(np.array(np.copy(MatrixStack.currMatrix)))
    
    def popMatrix():
        MatrixStack.currMatrix = MatrixStack.matricies.pop()

def offset(theta):
    z = math.sin(math.radians(theta)) * MOVESPEED
    x = math.cos(math.radians(theta)) * MOVESPEED
    return x,z

def draw(edgelist):
    worldToCamera = np.matmul( makeRotationMatrix(Camera.xrot), makeTransformMatrix(Camera.x, Camera.y, Camera.z)).T
    clipAndProjection = MatrixStack.clipAndProjection
    screenSpace = MatrixStack.screenSpace
    modelToWorld = MatrixStack.currMatrix
    for s in edgelist:
        p1,p2 = np.matmul( modelToWorld, np.array([s.start.x,s.start.y,s.start.z,1.0])), np.matmul(modelToWorld, np.array([s.end.x,s.end.y,s.end.z,1.0])) 
        cameraSpace1 = np.matmul(p1, worldToCamera)
        
        clipSpace1 = np.matmul(cameraSpace1, clipAndProjection)
        cameraSpace2 = np.matmul(p2,worldToCamera )
        clipSpace2 = np.matmul(cameraSpace2, clipAndProjection )
        
        clipSpace1, clipSpace2 = np.array(clipSpace1[0,:]), np.array(clipSpace2[0,:])
        ignore = False
        for test in [left,right,bottom,top,near,far]:
            if test(clipSpace1, clipSpace2):
                ignore = True
                break
        if ignore:
            continue
        p1x,p1y = clipSpace1[0][0]/clipSpace1[0][3], clipSpace1[0][1]/clipSpace1[0][3]
        p2x,p2y = clipSpace2[0][0]/clipSpace2[0][3], clipSpace2[0][1]/clipSpace2[0][3]
        screen1x, screen1y, scren1z = np.matmul(screenSpace, np.array([p1x,p1y,1.0]), )
        screen2x, screen2y, screen2z = np.matmul(screenSpace, np.array([p2x,p2y,1.0]), )
        pygame.draw.line(screen,BLUE,(screen1x, screen1y), (screen2x,screen2y))


def drawHouseOffset(x,z,rot):
    MatrixStack.pushMatrix()
    MatrixStack.currMatrix = np.matmul(makeTransformMatrix(-x,0,-z), makeRotationMatrix(rot))
    # print(MatrixStack.currMatrix)
    draw(loadHouse())
    MatrixStack.popMatrix()

def drawCarOffset(time):
    MatrixStack.pushMatrix()
    MatrixStack.currMatrix = np.matmul(MatrixStack.currMatrix, makeTransformMatrix( -((time/1000) - 5),0,-5))
    draw(loadCar())
    o = offset = 2
    for x,z in [(o,o), (-o,-o), (o,-o), (-o,o)]:
        drawTireOffset(x,z,time)
    MatrixStack.popMatrix()

def drawTireOffset(x,z,time):
    MatrixStack.pushMatrix()
    MatrixStack.currMatrix = np.matmul(MatrixStack.currMatrix, np.matmul(makeTransformMatrix(x,0,z), makeZRotationMatrix( -time/20) ) )
    draw(loadTire())
    MatrixStack.popMatrix()


while not done:
 
    # This limits the while loop to a max of 100 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)

    # Clear the screen and set the screen background
    screen.fill(BLACK)
    

    #Controller Code#
    #####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done=True
            
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        x,z = offset(Camera.xrot+180)
        Camera.x, Camera.z = Camera.x + x, Camera.z + z
    if pressed[pygame.K_w]:
        x,z = offset(Camera.xrot + 90)
        Camera.x, Camera.z = Camera.x + x, Camera.z + z
    if pressed[pygame.K_s]:
        x,z = offset(Camera.xrot-90)
        Camera.x, Camera.z = Camera.x + x, Camera.z + z
    if pressed[pygame.K_d]:
        x,z = offset(Camera.xrot)
        Camera.x, Camera.z = Camera.x + x, Camera.z + z
    if pressed[pygame.K_r]:
        Camera.y += MOVESPEED
    if pressed[pygame.K_f]:
        Camera.y -= MOVESPEED
    if pressed[pygame.K_e]:
        Camera.xrot -= ROTSPEED
    if pressed[pygame.K_q]:
        Camera.xrot += ROTSPEED
    if pressed[pygame.K_h]:
        Camera.x, Camera.y, Camera.z, Camera.xrot = 0,3,-5,0
        Car.startTime = pygame.time.get_ticks()
    # draw(loadHouse())
    drawHouseOffset(0,15,180)
    drawHouseOffset(-15,15,180)
    drawHouseOffset(15,15,180)
    drawHouseOffset(-35,0,90)


    drawHouseOffset(0,-15,0)
    drawHouseOffset(-15,-15,0)
    drawHouseOffset(15,-15,0)

    drawCarOffset(pygame.time.get_ticks() - Car.startTime)


        

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
