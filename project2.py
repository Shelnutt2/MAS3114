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

#Check to make sure atleast two rows are inputed
if not len(args.Rows) >= 2:
    parser.error("Please input atleast two rows")
#Check if the matrix is square
for r in args.Rows:
   if not len(args.Rows) == len(r):
      parser.error("The matrix you entered is not square")

#Functions to check invertibility
#Again here eps is used because of floating points and the inaccuracy of computer.
#Typically you'd check for = 0 but with floating points we check if it's close enough to zero.
def invertible( M, eps = 1.0/(10**10) ): 
   if not numpy.linalg.det(M) or abs(numpy.linalg.det(M)) <= eps: 
      print "The matrix is not invertible"
      return False
   else:
      return True

#Inverse using cramer's method
def cramer_inverse( M ):
   if invertible(M): #If it's invertible...
      adjM = numpy.array([],float) #Create a new floating point adj matrix.
      for r in range(len(M)):
         for c in range(len(M[r])): #Here we preform cramer's method on every entry in the matrix
            adjM = numpy.append(adjM,(-1)**(r+c)*numpy.linalg.det(numpy.delete(numpy.delete(M,c,1),r,0)))
      adjM = (numpy.reshape(adjM,(len(M[0]),len(M)))).transpose() #reshape the matrix and transpose it to get the true adj matrix
      invM = 1/numpy.linalg.det(M) * adjM #Find the inverse matrix
      return invM #Return the inverse matrix

 
narray = numpy.array(args.Rows)  #convert python list, to numpy array
narray = narray.astype(numpy.float) #Set array type to floating point

print "The Matrix you inputed is: \n" + str(narray)
print "The inverse of the inputed matrix is:"
print(cramer_inverse(narray)) #Print output matrix
