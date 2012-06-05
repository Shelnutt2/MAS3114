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
parser.add_argument('-s', '--solve', action='store', type=bool, metavar='Rows', type=eval, nargs='+', help='Rows of the matrix')

#initialize the arguments
args = parser.parse_args()

#Check to make sure only two vectors are inputed
if not len(args.Vectors) == 2:
    parser.error("Please input atleast two rows")


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

def ref( M ) :
   


mat = []
for r in args.Rows:
   mat.append(r)
 
rref( mtx )
 


