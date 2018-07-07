# Output:
# 
# Machines: 3
# Items: 5
# 	  M/c 1 | M/c 2 | M/c 3 | 
# ------------------------------------
# Job1	| 16	18	12
# Job2	| 14	10	11
# Job3	| 13	20	15
# Job4	| 19	15	19
# Job5	| 15	16	16
# [[16, 18, 12], [14, 10, 11], [13, 20, 15], [19, 15, 19], [15, 16, 16]]
# Original PT matrix
# 1 [16, 18, 12]
# 2 [14, 10, 11]
# 3 [13, 20, 15]
# 4 [19, 15, 19]
# 5 [15, 16, 16]
# PT matrix according to sequence
# 3 [13, 20, 15]
# 5 [15, 16, 16]
# 4 [19, 15, 19]
# 2 [14, 10, 11]
# 1 [16, 18, 12]
# Makespan
# [[ 13.  33.  48.]
#  [ 28.  44.  60.]
#  [ 47.  62.  81.]
#  [ 61.  71.  82.]
#  [ 77.  95. 107.]]

import numpy as np
import InputPTMatrix as PTmatrix

def main():
    #PT=[]
    machines=int(input("Machines: "))
    items=int(input("Items: "))
    seq=[3,5,4,2,1]
    #PT=[[16,18,12],[14,10,11],[13,20,15],[19,15,19],[15,16,16]]
    PT=PTmatrix.take_input(machines, items)
    
    items=len(PT)
    machines=len(PT[0])
    
    print("Original PT matrix")
    for j in range(0,items):
        print(j+1, PT[j])

    if len(seq) == 0:
        plain_makespan(PT, items, machines)
    elif len(seq) == items:
        seq_makespan(PT, items, machines, seq)
    else:
        print("Some items haven't been assigned a position in the sequence.")
        quit()

def plain_makespan(PT, items, machines):
    ms=np.zeros((items, machines))
    
    for j in range(0, items):
        ms[j][0]=ms[j-1][0]+PT[j][0]

        for m in range(0, machines-1):
            if ms[j][m] < ms[j-1][m]:
                ms[j][m+1]=ms[j-1][m]+PT[j][m+1]
            else:
                ms[j][m+1]=ms[j][m]+PT[j][m+1]

    print(ms)

def seq_makespan(PT, items, machines, seq):
    ms=np.zeros((items, machines))
    
    new_PT=[]
    print("PT matrix according to sequence")
    for s in seq:
        new_PT.append(PT[s-1])
        print(s, PT[s-1])

    print("Makespan")
    plain_makespan(new_PT, items, machines)

if __name__=="__main__":
    main()
