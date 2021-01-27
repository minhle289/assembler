#assuming all registers are 0
#the loop should run five times
#and registers 1- should all contain 3
#anything else, and your branching fails
addi $1 $0 1
addi $2 $0 1
addi $3 $0 3
beq $1 $3 3   #should  be taken on third loop
addi $1 $1 1
addi $2 $2 1
beq $1 $1 -4  #should always be taken, branch back to first beq
