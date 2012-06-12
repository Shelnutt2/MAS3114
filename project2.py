#!/bin/python

#MAS3114
#Project 1
#Seth Shelnutt


#Released under the GPL v3 or later

import argparse
import numpy

# Argument parser to parse user unput
parser = argparse.ArgumentParser(description='This is a program take input rows of a matrix and solve to (reduced) row echelon form.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.5')
parser.add_argument('Rows', metavar='Rows', type=eval, nargs='+', help='Rows of the matrix')


#initialize the arguments
args = parser.parse_args()

#Check to make sure only two vectors are inputed
if not len(args.Rows) >= 2:
    parser.error("Please input atleast two rows")
for r in args.Rows:
   if not len(args.Rows) == len(r):
      parser.error("The matrix you entered is not square")

def invertible( M ):
   if not numpy.linalg.det(M) or numpy.linalg.det(M) == 0:
      print "The matrix is not invertible"
      return False
   else:
      return True

def cramer_inverse( M ):
   if invertable(M):
      adjM = numpy.array([],float)
      for r in range(len(M)):
         for c in range(len(M[r])):
            adjM = numpy.append(adjM,(-1)**(r+c)*numpy.linalg.det(numpy.delete(numpy.delete(M,c,1),r,0)))
      adjM = numpy.reshape(adjM,(len(M[0]),len(M)))
      invM = 1/numpy.linalg.det(M) * adjM
      return invM

 
narray = numpy.array(args.Rows)  #convert python list, to numpy array
narray = narray.astype(numpy.float) #Set array type to floating point
 
print(cramer_inverse(narray))
