import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Define some constants
window_size = (800, 600)
sphere_radius = 0.5
small_sphere_radius = 0.3
sphere_position = [0, 0, -5]
small_sphere_position = [1, 1, -5]
sphere_rotation = [0, 0, 0]
small_sphere_rotation = [0, 0, 0]

# Initialize PyGame
pygame.init()

# Set up the window
pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)

# Initialize GLUT
glutInit()

# Set the display mode for GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

# Set up the projection matrix
# glMatrixMode — specify which matrix is the current matrix
glMatrixMode(GL_PROJECTION)
# view angle, aspect, zNear, zFar
gluPerspective(45, (window_size[0]/window_size[1]), 0.1, 50.0)

# Set up the modelview matrix
# glMatrixMode — specify which matrix is the current matrix
glMatrixMode(GL_MODELVIEW)
# glLoadIdentity — replace the current matrix with the identity matrix
glLoadIdentity()

# Enable depth testing
# glEnable — enable or disable server-side GL capabilities
# To enable depth testing, call glEnable with GL_DEPTH_TEST.
glEnable(GL_DEPTH_TEST)

# Define a function to draw a sphere
def draw_sphere(position, rotation, radius, color):
    glPushMatrix()
    glTranslate(position[0], position[1], position[2])
    glRotate(rotation[0], 1, 0, 0)
    glRotate(rotation[1], 0, 1, 0)
    glRotate(rotation[2], 0, 0, 1)
    glColor3f(color[0], color[1], color[2])
    #"""
    #radius
    #The radius of the sphere.
    #slices
    #The number of subdivisions around the Z axis (similar to lines of longitude).
    #stacks
    #The number of subdivisions along the Z axis (similar to lines of latitude).
    #"""
    glutSolidSphere(radius, 32, 32)
    glPopMatrix()

# Set up a clock to control the framerate
clock = pygame.time.Clock()

# Enter the main loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        # KEYDOWN: when the keyboard buttons are pressed
        # KEYUP: when the keyboard buttons are released
        elif event.type == KEYDOWN:
            if event.key == K_f:
                sphere_position[2] += 0.1
                small_sphere_position[2] += 0.1
            elif event.key == K_LEFT:
                sphere_rotation[1] -= 5
            elif event.key == K_RIGHT:
                sphere_rotation[1] += 5

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the spheres
    draw_sphere(sphere_position, sphere_rotation, sphere_radius, (1, 0, 0)) # Red sphere
    draw_sphere(small_sphere_position, small_sphere_rotation, small_sphere_radius, (0, 0, 1)) # Blue sphere

    # Swap buffers
    pygame.display.flip()

    # Control the framerate
    clock.tick(60)

