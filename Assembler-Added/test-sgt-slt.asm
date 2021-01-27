#presuming all registers begin with value 0
addi $1 $0 2
addi $2 $0 -2
addi $5 $0 1
addi $6 $0 1
sgt $3 $1 $0  #test the true cases
slt $4 $2 $0
sgt $5 $0 $1  #test the null cases
slt $6 $0 $2
