#!/bin/python

#MAS3114
#Project 1
#Seth Shelnutt


#Released under the GPL v3 or later

from matplotlib import pyplot
from mpl_toolkits.mplot3d import axes3d
import numpy, argparse


# Argument parser to parse user unput
parser = argparse.ArgumentParser(description='This is a program to draw a 2d plane based on a set of vectors.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.5')
parser.add_argument('Vectors', metavar='Vectors', type=eval, nargs='+', help='arrays for the plot')

#initialize the arguments
args = parser.parse_args()

#Check to make sure only two vectors are inputed
if not len(args.Vectors) == 2:
    parser.error("Please input two vectors")

print("These are the vectors you inputed")
print(args.Vectors)
x = []
y = []
z = []

for i in args.Vectors:
   x.append(i[0])
   y.append(i[1])
   z.append(i[2])



n = len(x) #Get length of each vector
m = len(y) 
o = len(z)
print("These are the the parametric vectors")
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
 
figure = pyplot.figure( 0 ) # Initialize out 3d plot
ax = axes3d.Axes3D( figure ) 
x = numpy.array( [ [ t ] * m for t in x ] ) # create output vectors of correct dimensions here
y = numpy.array( [ y ] * n )
z = numpy.array( [ z ] * o )

wire = ax.plot_surface( x, y, z,rstride=1, cstride=1 ) #  set the plot to surface type
figure.show() #show surface
pyplot.show() #show entire plot


