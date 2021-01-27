# Minh Le
# CSC270 FINAL PROJECT
# SKELETON ASSEMBLER BASED ON JOHN'S ASSEMBLER 

import sys
import helperfunctions
from helperfunctions import *

opcodeDict = {'add':'0000000', 'and': '00000001', 'or': '00000010', 'sub':'00000011', 'addi': '00100000', 'lw':'00101000', 'sw':'00110000', 'slt':'00000100', 'sgt':'00000101', 'beq':'01000011', 'j': '10000000', 'jr' : '11000000', 'jal':'10001000'}

def ConvertAssemblyToMachineCode(inline):
	'''given a string corresponding to a line of assembly,
	strip out all the comments, parse it, and convert it into
	a string of binary values'''

	outstring = ''

	if inline.find('#') != -1:
		inline = inline[0:inline.find('#')] #get rid of anything after a comment
	if inline != '':
		words = inline.split() #assuming syntax words are separated by space, not comma
		operation = words[0]
                outstring += opcodeDict[operation]
		operands = words[1:]
                if operation == "lw" or operation == "sw":
                        reg1 = operands[0]
                        other = operands[1]
                        if other[0] == '-':
                                offset = '-'
                                offset += other[1]
                                reg2 = other[4]
                        else:
                                offset = other[0]
                                reg2 = other[3]
                                        
                                outstring += int2bs(reg1[1:], 3)
                                outstring += int2bs(reg2[0:], 3)
                                outstring += int2bs(offset[0:], 3)
                                
                elif operation == 'j' or operation == 'jal' or operation == 'jr':
                        outstring += int2bs(operands[0],9)
                else:
                        for oprand in operands:
			        # R-type instructions
			        if oprand[0] == '$':
				        outstring += int2bs(oprand[1:],3)
                                else:
                                        outstring += int2bs(oprand[0:],3)
      	return outstring	
 	

def AssemblyToHex(infilename,outfilename):
	'''given an ascii assembly file , read it in line by line and convert each line of assembly to hex code
	then save that machinecode to an outputfile'''
	outlines = []
	with open(infilename) as f:
		lines = [line.rstrip() for line in f.readlines()]  #get rid of \n whitespace at end of line
		for curline in lines:
			outstring = ConvertAssemblyToMachineCode(curline)
                        if outstring != '':
                                outstring = bs2hex(outstring)
				outlines.append(outstring)
                              
	f.close()

	with open(outfilename,'w') as of:
                of.write("v2.0 raw")
                of.write("\n")
		for outline in outlines:
			of.write(outline)
			of.write("\n")
	of.close()		
			

if __name__ == "__main__":
	#in order to run this with command-line arguments
	# we need this if __name__ clause
	# and then we need to read in the subsequent arguments in a list.
	
	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args	
	if (len(sys.argv) != 3):
		print('usage: python skeleton-assembler.py inputfile.asm outputfile.hex')
		exit(0)
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	AssemblyToHex(inputfile,outputfile)


