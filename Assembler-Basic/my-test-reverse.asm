#Reverse contents in data memory
addi $3 $0 3
addi $4 $3 1       
addi $5 $4 1

lw $1 0($0)
lw $2 0($5)
sw $1 0($5)
sw $2 0($0)

lw $1 1($0)
lw $2 0($4)
sw $1 0($4)
sw $2 1($0)

lw $1 2($0)
lw $2 3($0)
sw $1 3($0)
sw $2 2($0)



