This assembler translates assembly code into hexadecimal machine language which can be directly load into Logisim’s CPU. Here, I’m using 16-bit instruction with 8-bit opcode and 9-bit for registers (3 registers, 3-bit each).

The translation process is based on the basic assembler with added cases for jump