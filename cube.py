"""
This is a side project to try and project a
cube in an orthographic perspective on a 2D
plane using Python's turtle module

This uses a module I wrote to perform matrix operations

author: Elijah Kliot
"""

from math import *
from turtle import *
from matrices import *


"""
rotates a 3D coordinate by a given angle of rotation on each axis

point -- a list of length 3 with an x, y, and z co ordinate
rotX  -- an angle of rotation along the x axis in radians
rotY  -- an angle of rotation along the y axis in radians
rotZ  -- an angle of rotation along the z axis in radians

returns a matrix composed of the transformed x, y, and z values
"""
def rotation( point, rotX, rotY, rotZ ):

    point  = pointMatrix( point[ 0 ], point[ 1 ], point[ 2 ] )
    transX = matrixMult( rotXMatrix( rotX ), point )
    transY = matrixMult( rotYMatrix( rotY ), transX )
    transZ = matrixMult( rotZMatrix( rotZ ), transY )
    rotPt  = transZ

    return rotPt

"""
converts a matrix with 3D co ordinates into 2D co-ordinates

point :: 3x3 matrix :: a 3D co ordinate matrix

returns a matrix with the x and y values of a projected 2D co ordinate
"""
def projection( point ):
    projPt = matrixMult( transMatrix(), point )
    finPt = []

    for row in range( len( projPt ) - 1 ):
        finPt.append( projPt[ row ][ 0 ] )

    return finPt

"""
draws a cube using turtle by drawing an edge between each corner
cube starts at a 'home' rotation with the face ABDC parallel to the monitor

size :: int :: the side-length of the cube to be drawn
rotX :: float :: an angle of rotation along the x axis in radians
rotY :: float :: an angle of rotation along the y axis in radians
rotZ :: float :: an angle of rotation along the z axis in radians

returns None
"""
def cube( size, rotX, rotY, rotZ ):

      # compute the diagonals
    sqrDiag = sqrt( 2 * ( size ** 2 ) )
    cubeDiag = sqrt( ( sqrDiag ** 2 ) + ( size ** 2 ) )

      # 'home' co ordinates for each corner
    ptA = [ -(size*.5),  (size*.5),  (size*.5) ]
    ptB = [  (size*.5),  (size*.5),  (size*.5) ]
    ptC = [ -(size*.5), -(size*.5),  (size*.5) ]
    ptD = [  (size*.5), -(size*.5),  (size*.5) ]
    ptE = [ -(size*.5),  (size*.5), -(size*.5) ]
    ptF = [  (size*.5),  (size*.5), -(size*.5) ]
    ptG = [ -(size*.5), -(size*.5), -(size*.5) ]
    ptH = [  (size*.5), -(size*.5), -(size*.5) ]

      # Converts each point to its rotated 3D value
    ptARot = rotation( ptA, rotX, rotY, rotZ )
    ptBRot = rotation( ptB, rotX, rotY, rotZ )
    ptCRot = rotation( ptC, rotX, rotY, rotZ )
    ptDRot = rotation( ptD, rotX, rotY, rotZ )
    ptERot = rotation( ptE, rotX, rotY, rotZ )
    ptFRot = rotation( ptF, rotX, rotY, rotZ )
    ptGRot = rotation( ptG, rotX, rotY, rotZ )
    ptHRot = rotation( ptH, rotX, rotY, rotZ )

      # Converts each 3D point to a 2D point
    finA = projection( ptARot )
    finB = projection( ptBRot )
    finC = projection( ptCRot )
    finD = projection( ptDRot )
    finE = projection( ptERot )
    finF = projection( ptFRot )
    finG = projection( ptGRot )
    finH = projection( ptHRot )


      # drawing the cube, one edge at a time

      # draw AC, AB, AE
    drawLine( finA, finC )
    drawLine( finA, finB )
    drawLine( finA, finE )

      # draw EG, EF
    drawLine( finE, finG )
    drawLine( finE, finF )

      # draw FB, FH
    drawLine( finF, finB )
    drawLine( finF, finH )

      # draw HG, HD
    drawLine( finH, finG )
    drawLine( finH, finD )

      # draw DB, DC
    drawLine( finD, finB )
    drawLine( finD, finC )

      # draw CG
    drawLine( finC, finG )

def drawLine( pt1, pt2 ):
    pos = position()

    up()
    setpos(pt1)
    down()
    setpos(pt2)
    up()

    if pos != position():
        setpos(pos)

"""
animates the rotation of a cube from its 'home' position

size  :: int :: the side-length of the cube to be drawn
rotX  :: float :: final angle of rotation along the x axis in radians
rotY  :: float :: final angle of rotation along the y axis in radians
rotZ  :: float :: final angle of rotation along the z axis in radians
steps :: int :: the number of frames of animation

returns None
"""
def animateCube( size, rotX, rotY, rotZ, steps ):
      # an array of each sequential frame values
    frames = []

      # how much to be rotating for each axis, per step
    incX = rotX / steps
    incY = rotY / steps
    incZ = rotZ / steps

      # build the frame array
    for n in range( 0, steps + 1 ):
        frames.append( [ incX * n, incY * n, incZ * n ] )

      # execute an animation for each frame
    for f in frames:
        clear()
        cube( size, f[ 0 ], f[ 1 ], f[ 2 ] )

"""

"""
def main():
    ht()
    speed(0)

    while input("\n  Press enter to continue, input 'bye' to end... ") != 'bye':
        clear()

        size = int(input("  cube size?\n\t"))

        rotX = float(input("  x-axis rotation? (radians)\n\t"))
        rotY = float(input("  y-axis rotation? (radians)\n\t"))
        rotZ = float(input("  z-axis rotation? (radians)\n\t"))

        step = int(input("  how many steps?\n\t"))

        animateCube( size, rotX, rotY, rotZ, step )

    bye()

main()


"""
      E_________ F
     /|         /|
    / |        / |
  A___|_______B  |
  |   G_______|__|H
  |  /        | /
  | /         |/
 C|/__________|D

SIX FACES: # # #
    ABDC
    ABFE
    ACGE
    BDHF
    CDHG
    EFHG

Thought process

    EVERY CORNER IS ALWAYS AT AN (x,y,z) CO ORD ALONG A SPHERE OF RADIUS 1/2(cubeDiag)
    ptH's (x,y,z) is -1 * PtA, ptG to ptB, ptF to ptC, ptE to ptD

    Thus, the primary hurdle is to find how the rotation translates the corner at (x,y,z)

    At 'home' rotation, face ABDC is perpendicular to the monitor
    ptA is ( -(size*.5), (size*.5), (size*.5) ) at 'home' rotation
    ptB is ( (size*.5), (size*.5), (size*.5) ) at 'home' rotation
    ptC is ( -(size*.5), -(size*.5), (size*.5) ) at 'home' rotation
    ptD is ( (size*.5), -(size*.5), (size*.5) ) at 'home' rotation

    rotation on x axis transforms a point's y and z co ords
    rotation on y axis transforms a point's x and z co ords
    rotation on z axis transforms a point's x and y co ords

    Each point is the end of a line. Rotating this line about an axis generates a cone
    The radius of this cone is l*sin(p), where l is the line length and p is the angle of the line to the axis being rotated around
    The bottom face of this cone is a circle with that radius, at a value l*cos(p) along the axis being rotated around, perpendicular to the axis
    Rotation around that axis will translate the point along the circumference of that circle

    rotation on x axis by p degrees translates the y value by sin(p) and the z value by -cos(p)
    rotation on y axis by p degrees translates the x value by cos(p) and the z value by -sin(p)
    rotation on z axis by p degrees translates the x value by cos(p) and the y value by sin(p)
"""
