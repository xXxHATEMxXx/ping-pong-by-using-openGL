from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi,sqrt,sin,cos

window = 0                                             # glut window number
width, height = 800, 800                               # window size
r1=[20, 20, 200, 20]
r2=[20, 760, 200, 20]
c1 = [50, 200, 200, 100]
m=0                                         # m=0 == ball move right and up ,  m=1 means ball move right and down , m=2 means ball move left and up , m=3 means ball move left and down 


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d
    # ToDo draw rectangle
    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_rect(r1)                         # rect at (10, 10) with width 200, height 100
    draw_rect(r2)
    draw_circle(c1)
    rectangle_boder_collision(r1 , r2)
    animation_section()
    ball_border_collition()
    ball_rectangle_collition()
    




    glutSwapBuffers()                                  # important for double buffering
   
def draw_rect(r):                    # r=[x, y, width, height]                          # done drawing a rectangl
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(r[0], r[1])                                   # bottom left point
    glVertex2f(r[0] + r[2], r[1])                           # bottom right point
    glVertex2f(r[0] + r[2], r[1] + r[3])                  # top right point
    glVertex2f(r[0], r[1] + r[3])                          # top left point
    glEnd()  

def draw_circle(c):           #c=[radius , x_c , y_c , steps]
    glBegin(GL_POLYGON)    
    dtheta = 2*pi / c[3] 
    theta = 0 
    while theta <= 2*pi : 
        x = int (c[1] + c[0] * cos(theta))
        y = int (c[2] + c[0] * sin(theta)) 
        theta += dtheta 
        glVertex2i(x,y)
    glEnd()

def rectangle_boder_collision(r1 , r2):
    #for r2
    if c1[1]>=700:
        r2[0]=600
    elif c1[1]<=100:
        r2[0]=0
    else:
        r2[0]=c1[1]-(r2[2]*.5)
    
    #for r1
    if r1[0]>=600:
        r1[0]=600
    elif r1[0]<=0:
        r1[0]=0

def animation_section():  # m=0 == ball move right and up ,  m=1 means ball move right and down , m=2 means ball move left and up , m=3 means ball move left and down 
    global m
    if m==0:
        c1[1]+=.1
        c1[2]+=.1
    elif m==1:
        c1[1]+=.1
        c1[2]-=.1
    elif m==2:
        c1[1]-=.1
        c1[2]+=.1
    elif m==3:
        c1[1]-=.1
        c1[2]-=.1

def ball_border_collition(): 
    global m
    if c1[1]+c1[0]>=width and m==0:
        m=2

    elif c1[1]+c1[0]>=width and m==1:
        m=3

    elif c1[1]-c1[0]<=0 and m==3:
        
        m=1
    elif c1[1]-c1[0]<=0 and m==2 :
        
        m=0
def ball_rectangle_collition():  #c=[radius , x_c , y_c , steps]
    global m
    if c1[2]+c1[0]>=r2[1] and m==0:
        
        m=1
    elif c1[2]+c1[0]>=r2[1] and m==2:
        
        m=3
    
    elif c1[2]-c1[0]<=r1[1]+r1[3] and m==1 and c1[1]>=r1[0] and c1[1]+c1[3]<=r1[0]+r1[2] and c1[2]<=20:
        
        glutLeaveMainLoop()
        import gameover_screen
        glutDestroyWindow()
        
    elif c1[2]-c1[0]<=r1[1]+r1[3] and m==3 and c1[1]>=r1[0] and c1[1]+c1[3]<=r1[0]+r1[2] and c1[2]<=20:
        
        glutLeaveMainLoop()
        import gameover_screen
        glutDestroyWindow(window)

        
    elif c1[2]-c1[0]<=r1[1]+r1[3] and m==1 and c1[1]>=r1[0] and c1[1]+c1[3]<=r1[0]+r1[2] :
    
        m=0
    elif c1[2]-c1[0]<=r1[1]+r1[3] and m==3 and c1[1]>=r1[0] and c1[1]+c1[3]<=r1[0]+r1[2]:
        
        m=2
        

def keys(k , x , y):
     
    # HINT : update the r1 list to 
    if k==GLUT_KEY_RIGHT  :
        r1[0] +=20

    elif k==GLUT_KEY_LEFT :
        r1[0]-=20


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
while True:    # initialization
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(600, 150)                           # set window position
    window = glutCreateWindow("PingPong")              # create window with title
    glutSpecialFunc(keys)
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()                                         # start everything