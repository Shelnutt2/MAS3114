#!/bin/python

#MAS3114
#Project 1
#Seth Shelnutt


#Released under the GPL v3 or later

import argparse

# Argument parser to parse user unput
parser = argparse.ArgumentParser(description='This is a program to draw a 2d plane based on a set of vectors.')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.5')
parser.add_argument('Vectors', metavar='Vectors', type=eval, nargs='+', help='arrays for the plot')

#initialize the arguments
args = parser.parse_args()

def reff(m, eps = 1.0/(10**10)):
  rownum, columnnum = (len(m),len(m[0]))
  for y in range(0,rownum):
    lastrow = y
    for y2 in range(y+1, rownum):    # Find max pivot
      if abs(m[y2][y]) > abs(m[lastrow][y]):
        lastrow = y2
    (m[y], m[lastrow]) = (m[lastrow], m[y])
    if abs(m[y][y]) <= eps:     # Singular?
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
  return True

def ToReducedRowEchelonForm( M):
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
 
 
mtx = [
   [ 1, 2, -1, -4],
   [ 2, 3, -1, -11],
   [-2, 0, -3, 22],]
 
ToReducedRowEchelonForm( mtx )
 
for rw in mtx:
  print ', '.join( (str(rv) for rv in rw) )



p1 = [[1, 2, -1, -4],[2, 3, -1, -11],[-2, 0, -3, 22]]
print p1
reff(p1)
print p1
