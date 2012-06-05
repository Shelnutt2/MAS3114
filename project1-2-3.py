#!/bin/python

#MAS3114
#Project 1
#Seth Shelnutt


#Released under the GPL v3 or later

import argparse

# Argument parser to parse user unput
parser = argparse.ArgumentParser(description='This is a program to draw a 2d plane based on a set of vectors.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.5')
parser.add_argument('Rows', metavar='Rows', type=eval, nargs='+', help='Rows of the matrix')
parser.add_argument('-s', '--solve', action='store', type=bool, metavar='solve', help='Solve for variables')
parser.add_argument('-r', '--reduce', action='store', type=bool, metavar='reduce', help='reduce to reduced row echlon form')

#initialize the arguments
args = parser.parse_args()

#Check to make sure only two vectors are inputed
if not len(args.Rows) == 2:
    parser.error("Please input atleast two rows")

def ref( M ):
   for rnum in range(len(M)) :
      if M[rnum][rnum] == 0 :
	     #rnump = 0
         if rnum +1 <= len(M) :
		    rnump = rnum+1
         else:
		    rnump = rnum
         mtemp = M[rnum]
         M[rnum] = M[rnump]
         M[rnump] = mtemp
      if not M[rnum][rnum] == 0:
         print M[rnum]
         print M[rnum][rnum]
         number = M[rnum][rnum]
         print number
         M[rnum] = [ mrow/number for mrow in M[rnum] ]
      for nrnum in range(len(M)-1):
         if not M[nrnum+1][rnum] == 0:
            var2 = M[nrnum+1][rnum]
            #var3 = M[rnum]
            for digit in range(len(M[rnum+1])-1):
               M[nrnum+1][digit] = [M[nrnum+1][digit] - var2*M[rnum][digit]]
	
def rref( M ):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
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


 
if(args.solve):
  p=1#solve functions
elif args.reduce:
   rref(args.Rows)
else:
   ref(args.Rows)