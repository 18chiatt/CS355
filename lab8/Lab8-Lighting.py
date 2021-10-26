""" Modified code from Peter Colling Ridge 
	Original found at http://www.petercollingridge.co.uk/pygame-3d-graphics-tutorial
"""

import pygame, math
import numpy as np
import wireframe as wf
import basicShapes as shape
cos = math.cos
sin = math.sin

class LightRotation:
    xrot = 0
    yrot = 0
    zrot = 0


def xRotMatrix(xrot):
    radians = math.radians(xrot)
    return np.array([
        [1,0,0],
        [0,cos(radians),-sin(radians)],
        [0,sin(radians),cos(radians)],
    ])

def yRotMatrix(yrot):
    radians = math.radians(yrot)
    return np.array([
        [cos(radians),0,sin(radians)],
        [0,1,0],
        [-sin(radians),0,cos(radians)],
    ])

def zRotMatrix(zrot):
    radians = math.radians(zrot)
    return np.array([
        [cos(radians),-sin(radians),0],
        [sin(radians),cos(radians),0],
        [0,0,1],
    ])

wRotMatrix_B = xRotMatrix(30)
sRotMatrix_B = xRotMatrix(-30)

qRotMatrix_B = zRotMatrix(30)
eRotMatrix_B = zRotMatrix(-30)


aRotMatrix_B = yRotMatrix(-30)
dRotMatrix_B = yRotMatrix(30)



# def rotateLight(light, xRot, yRot, zRot):
#     withZ = np.matmul(light, zRotMatrix(zRot))
#     withXY = np.matmul(withZ,yRotMatrix(yRot))
#     withXRot = np.matmul(withXY,xRotMatrix(xRot))
#     return withXRot

class WireframeViewer(wf.WireframeGroup):
    """ A group of wireframes which can be displayed on a Pygame screen """
    
    def __init__(self, width, height, name="Wireframe Viewer"):
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        
        self.wireframes = {}
        self.wireframe_colours = {}
        self.object_to_update = []
        
        self.displayNodes = False
        self.displayEdges = True
        self.displayFaces = True
        
        self.perspective = False
        self.eyeX = self.width/2
        self.eyeY = 100
        self.light_color = np.array([1,1,1])
        self.view_vector = np.array([0, 0, -1])        
        self.light_vector = np.array([0, 0, -1])  

        self.background = (10,10,50)
        self.nodeColour = (250,250,250)
        self.nodeRadius = 4
        
        self.control = 0
    
    def addWireframe(self, name, wireframe):
        self.wireframes[name] = wireframe
        #   If colour is set to None, then wireframe is not displayed
        self.wireframe_colours[name] = (250,250,250)
    
    def addWireframeGroup(self, wireframe_group):
        # Potential danger of overwriting names
        for name, wireframe in wireframe_group.wireframes.items():
            self.addWireframe(name, wireframe)
    
    def display(self):
        self.screen.fill(self.background)
        light_vector = self.light_vector
        light_color = self.light_color
        v = self.view_vector
        v = v / np.linalg.norm(v)
        L = light_vector
        k_specular = .3
        k_gls = 8
        k_diffuse = .4
        m_ambient = 0.3
        for name, wireframe in self.wireframes.items():
            nodes = wireframe.nodes
            
            if self.displayFaces:
                for (face, colour) in wireframe.sortedFaces():
                    v1 = (nodes[face[1]] - nodes[face[0]])[:3]
                    v2 = (nodes[face[2]] - nodes[face[0]])[:3]

                    normal = np.cross(v1, v2)
                    normal /= np.linalg.norm(normal)
                    towards_us = np.dot(normal, self.view_vector)


                    # Only draw faces that face us
                    if towards_us > 0:
                        N = normal
                        
                        ambient = self.light_color * (m_ambient * colour)

                        if np.dot(normal, light_vector) > 0:
                            diffuse = k_diffuse * np.multiply(light_color, colour) * (np.dot(N, L))
                            R = (2 * (np.dot(L,N)) * N) - L
                            specular = k_specular * np.multiply(light_color, colour) * math.pow((np.dot(v,R)),k_gls)
                            light_total = ambient + diffuse + specular
                        else:
                            # print("Only ambient")
                            light_total = ambient
                        light_total = np.clip(light_total,0,255)

                        pygame.draw.polygon(self.screen, light_total, [(nodes[node][0], nodes[node][1]) for node in face], 0)

                if self.displayEdges:
                    for (n1, n2) in wireframe.edges:
                        if self.perspective:
                            if wireframe.nodes[n1][2] > -self.perspective and nodes[n2][2] > -self.perspective:
                                z1 = self.perspective/ (self.perspective + nodes[n1][2])
                                x1 = self.width/2  + z1*(nodes[n1][0] - self.width/2)
                                y1 = self.height/2 + z1*(nodes[n1][1] - self.height/2)
                    
                                z2 = self.perspective/ (self.perspective + nodes[n2][2])
                                x2 = self.width/2  + z2*(nodes[n2][0] - self.width/2)
                                y2 = self.height/2 + z2*(nodes[n2][1] - self.height/2)
                                
                                pygame.draw.aaline(self.screen, colour, (x1, y1), (x2, y2), 1)
                        else:
                            pygame.draw.aaline(self.screen, colour, (nodes[n1][0], nodes[n1][1]), (nodes[n2][0], nodes[n2][1]), 1)

            if self.displayNodes:
                for node in nodes:
                    pygame.draw.circle(self.screen, colour, (int(node[0]), int(node[1])), self.nodeRadius, 0)
        
        pygame.display.flip()

    def keyEvent(self, key):
        rot_speed = 10
        #Your code here
        if key == pygame.K_w:
            self.light_vector = np.matmul(self.light_vector,wRotMatrix_B)

        if key == pygame.K_s:
            self.light_vector = np.matmul(self.light_vector,sRotMatrix_B)

        if key == pygame.K_a:
            self.light_vector = np.matmul(self.light_vector,aRotMatrix_B)


        if key == pygame.K_d:
                self.light_vector = np.matmul(self.light_vector,dRotMatrix_B)

        if key == pygame.K_q:
            self.light_vector = np.matmul(self.light_vector,qRotMatrix_B)

        if key == pygame.K_e:
            self.light_vector = np.matmul(self.light_vector,eRotMatrix_B)

        return

    def run(self):
        """ Display wireframe on screen and respond to keydown events """
        
        running = True
        key_down = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    key_down = event.key
                elif event.type == pygame.KEYUP:
                    key_down = None
            
            if key_down:
                self.keyEvent(key_down)
            
            self.display()
            self.update()
            
        pygame.quit()

		
resolution = 52
viewer = WireframeViewer(600, 400)
viewer.addWireframe('sphere', shape.Spheroid((300,200, 20), (160,160,160), resolution=resolution))

# Colour ball
faces = viewer.wireframes['sphere'].faces
for i in range(int(resolution/4)):
	for j in range(resolution*2-4):
		f = i*(resolution*4-8) +j
		faces[f][1][1] = 0
		faces[f][1][2] = 0
	
viewer.displayEdges = False
viewer.run()
