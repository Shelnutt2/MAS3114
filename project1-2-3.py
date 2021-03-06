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
parser.add_argument('-s', '--solve', action='store_true', dest='solve', help='Solve for variables')
parser.add_argument('-r', '--reduce', action='store_true', dest='reduce', help='reduce to reduced row echelon form')

#initialize the arguments
args = parser.parse_args()

#Check to make sure only two vectors are inputed
if not len(args.Rows) >= 2:
    parser.error("Please input atleast two rows")

def ref( M ):
   for rnum in range(len(M)) : #iterate through the rows
      if M[rnum][rnum] == 0 : #if the rows are zero we need to swap rows
         if rnum +1 <= len(M) : #Only swap if it's not the last row
		    rnump = rnum+1
         else:
		    rnump = rnum
         mtemp = M[rnum]
         M[rnum] = M[rnump]
         M[rnump] = mtemp
      if not M[rnum][rnum] == 0: #If the pivot position isn't zero we make it 1.
         M[rnum] = M[rnum]/M[rnum][rnum]
      if not rnum == len(M)-1:
         for nrnum in range(len(M)-1):
            if not M[nrnum+1][rnum] == 0:
		       M[nrnum+1] = M[nrnum+1]-M[nrnum+1][rnum]*M[rnum] #make all rows have zeros in the pivot positions
   return M

	
def rref( M ): #Secondary rref code. More percise but less accurate due to expecting zero.
    if not M[1][1]: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return "you matrix has more rows than columns!"
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / lv for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    return M
    
def rreff2(m, eps = 1.0/(10**10)):  #eps refers to how close to zero do we consider zero? 10^10 seems close enough
  rownum, columnnum = (len(m),len(m[0])) #Get dimension of matrix
  for y in range(0,rownum):  #Parse through each row
    lastrow = y              #Keep track of previous row
    for y2 in range(y+1, rownum):    # Find max pivot
      if abs(m[y2][y]) > abs(m[lastrow][y]):
        lastrow = y2
    (m[y], m[lastrow]) = (m[lastrow], m[y])
    if abs(m[y][y]) <= eps:     # Singular? Again we use eps because with floating points chances are we'll rarely actually get zero
      return False
    for y2 in range(y+1, rownum):    # Eliminate column y
      c = m[y2][y] / m[y][y]
      for x in range(y, columnnum):
        m[y2][x] -= m[y][x] * c
  for y in range(rownum-1, 0-1, -1): # Backsubstitute
    c  = m[y][y]
    for y2 in range(0,y):
      for x in range(columnnum-1, y-1, -1):
        m[y2][x] -=  m[y][x] * m[y2][y] / c
    m[y][y] /= c
    for x in range(rownum, columnnum):       # Normalize row y
      m[y][x] /= c
  return m    #Return the final matrix
 
 
narray = numpy.array(args.Rows)  #convert python list, to numpy array
narray = narray.astype(numpy.float) #Set array type to floating point
 
if(args.solve): #Outputs the answer in a nice format.
  vars2d = rreff2(narray)  
  print("x = " + str(vars2d[0][2]))
  print("y = " + str(vars2d[1][2]))
  
elif args.reduce: #If reduce flag is thrown we put it in reduced row echelon form
   print(rreff2(narray))
   
else:  #If nothing else we put it into row echelon form.
   print(ref(narray))
