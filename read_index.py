# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.
import parsing
import sys

arguments = len(sys.argv) - 1


position = 1

while (arguments >= position):
    print ("Paramter %i: %s" % (position, sys.argv[position]))
    position = position + 1

