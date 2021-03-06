##*******************************************************##
##                                                       ##
##                 DuplicateRemoval                      ##
##                                                       ##
##                   Kyle Strand                         ##
##               kyletstrand@gmail.com                   ##
##                                                       ##
##   Reads a text file and removes duplicate entries     ##
##   and creates a new file without the duplicates       ##
##   leaving the initial file intact.                    ##
##                                                       ##  
##*******************************************************##

import sys
from collections import OrderedDict

# Help input
def help():
   print "DuplicateRemoval reads input file, deletes duplicate entries, and writes to a new file.\n"
   print "Command structure: python DuplicateRemoval.py <input file> <new output file>"
   exit(0)

# Error function
def error():
   print "Command structure: python DuplicateRemoval.py <input file> <new output file>"
   exit(1)


for arg in sys.argv:
   if (arg == "--help" or arg == "-h"):
       help()

# select input file and name output file from command line argument
if (len(sys.argv) == 3):
   infile = sys.argv[1]
   outfile = sys.argv[2]
if (len(sys.argv) != 3):
      error()

print "Reading ",infile," and searching for duplicate entries...\n"
inf = open(infile,"r")
lines = inf.readlines()

inf.close()

newset = list(OrderedDict.fromkeys(lines))
outf = open(outfile,"w")
lstline = len(newset)
for i in range(0,lstline):
   ln = newset[i]
   outf.write(ln)
outf.close()

