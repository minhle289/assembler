This assembler translates assembly code into hexadecimal machine language which can be directly load into Logisim’s CPU. Here, I’m using 14-bit instruction with 5-bit opcode and 9-bit for registers (3 registers, 3-bit each).

First, given a input file, it goes through each line, get rid of all the comments, parse and convert it to a string of binary value. The operation (add, and, or, etc.) is translated to binary opcode using the opcodeDict specified at the beginning of the assembler. Due to the difference in the order of the registers in R-type versus LW/SW instructions, the assembler uses two separates ways when putting the assembly code into binary code, one for LW/SW and one for all other instructions. 

After the binary version of the machine code has been produced, the assembler will translate these strings of binary value into hex value (hexadecimal machine language) that can be run on the CPU. 

Finally, the assembler will save the line-by-line translation to an output file.