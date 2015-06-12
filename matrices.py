"""
this is a module to perform matrix operations

currently it performs matrix multiplication, using
matrices in the form of lists within lists, so that
the indeces of the lists correspond to the rows and
columns of a matrix

for example:
myMtx = [ [ a, b ], [ c, d ] ]
to access a is mtMtx[0][0], as it corresponds to
row 0 and column 0 in a matrix of form:
| a b |
| c d |

the matrices included as functions are:
+3D to 2D orthographic projection
+3D translation matrices for rotation along the x, y, and z axes
+a matrix representing a 3D coordinate (x,y,z)

Author: Elijah Kliot
"""

from math import *

def transMatrix():
    """
    returns a 3D to 2D orthographic projection matrix
    """
    matrix = [[ 1, 0, 0 ],
              [ 0, 1, 0 ],
              [ 0, 0, 0 ]]
    return matrix

def rotXMatrix( theta ):
    """
    theta -- angle of rotation in radians
    
    returns a matrix for rotation of a 3D coordinate
    around the X axis by theta degrees
    """
    matrix = [[ 1,            0,                 0 ],
              [ 0, cos( theta ), -( sin( theta ) ) ],
              [ 0, sin( theta ),    cos( theta )   ]]
    return matrix

def rotYMatrix( theta ):
    """
    theta -- angle of rotation in radians

    returns a matrix for rotation of a 3D coordinate
    around the Y axis by theta degrees
    """
    matrix = [[      cos( theta ), 0, sin( theta ) ],
              [                 0, 1,            0 ],
              [ -( sin( theta ) ), 0, cos( theta ) ]]
    return matrix

def rotZMatrix( theta ):
    """
    theta -- angle of rotation in radians

    returns a matrix for rotation of a 3D coordinate
    around the Z axis by theta degrees
    """
    matrix = [[ cos( theta ), -( sin( theta ) ), 0 ],
              [ sin( theta ),      cos( theta ), 0 ],
              [            0,                 0, 1 ]]
    return matrix

def pointMatrix( x, y, z ):
    """
    x; y; z -- coordinates for a point in a 3D plane

    returns a matrix for given 3D coordinates
    """
    matrix = [[ x ],
              [ y ],
              [ z ]]
    return matrix

def matrixMult( mat1, mat2 ):
    """
    mat1; mat2 -- any matrix of list-in-list format

    multiplies two matrices by building a product
    matrix based on the dimensions of the two matrices
    being multiplied, and then filling the product
    matrix with the results of multiplying the two
    matrices

    returns the product of the two matrices
    """
    
    #building the skeleton for the product matrix
    base = []
    for row in range( len( mat1 ) ):
        base.append( [] )
    for col in range( len( mat2[ 0 ] ) ):
        for row in range( len( base ) ):
            base[ row ].append( [] )

    #filling out the product matrix with the resulting values
    for row in range( len( base ) ):
        for col in range( len( base[ row ] ) ):
            for wor in range( len( mat2 ) ):
                base[ row ][ col ].append( mat1[ row ][ wor ] * mat2[ wor ][ col ] )

    #adding up the values for each row/column combo
    for row in range( len( base ) ):
        for col in range( len( base[ row ] ) ):
            tot = 0
            for e in range( len( base[ row ][ col ] ) ):
                tot += base[ row ][ col ][ e ]
            base[ row ][ col ] = tot

    return base
