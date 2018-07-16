

#   Output:
#                   Heurestics - Palmer Algorithm
#   Machines: 3
#   Items: 5
#   	  M/c 1 | M/c 2 | M/c 3 | 
#   ------------------------------------
#   Job1	| 16	18	12	
#   Job2	| 14	10	11
#   Job3	| 13	20	15
#   Job4	| 19	15	19
#   Job5	| 15	16	16
#   [[16, 18, 12], [14, 10, 11], [13, 20, 15], [19, 15, 19], [15, 16, 16]]
#   Makespan
#   [[ 16.  34.  46.]
#    [ 30.  40.  51.]
#    [ 43.  63.  78.]
#    [ 62.  77.  96.]
#    [ 77.  93. 109.]]
#   Calculated weights:  [-8, -6, 4, 0, 2]
#   Final sequence: 
#   3 [13, 20, 15]
#   5 [15, 16, 16]
#   4 [19, 15, 19]
#   2 [14, 10, 11]
#   1 [16, 18, 12]
#   PT matrix according to sequence
#   3 [13, 20, 15]
#   5 [15, 16, 16]
#   4 [19, 15, 19]
#   2 [14, 10, 11]
#   1 [16, 18, 12]
#   Makespan
#   [[ 13.  33.  48.]
#    [ 28.  44.  60.]
#    [ 47.  62.  81.]
#    [ 61.  71.  82.]
#    [ 77.  95. 107.]]

import InputPTMatrix as PTMatrix
import MeasureMakespanFunction as makespan
def main():
    print("Heurestics - Palmer")

    weights=[-2,0,2]
    #PT=[[16,18,12],[14,10,11],[13,20,15],[19,15,19],[15,16,16]]
    PT, items, machines=PTMatrix.take_input()
    
    makespan.plain_makespan(PT, items, machines)
    wt=measure_weights(PT, weights, items, machines)
    s=sort_with_wt(PT, wt,  items, machines)
    makespan.seq_makespan(PT, items, machines, s)
    
def measure_weights(PT, weights, items, machines):
    calculated_weights=[]

    for j in range(0, items):
        temp=[]
        for m in range(0, machines):
            temp.append(PT[j][m]*weights[m])
        calculated_weights.append(sum(temp))

    print("Calculated weights: ",calculated_weights)
    return calculated_weights

def sort_with_wt(PT, weights, items, machines):
    jobs=dict((key+1, PT[key]) for key in range(0, len(PT)))
    
    seq=list(range(1, items+1))
    for t in range(0, len(weights)):
        for w in range(0, len(weights)-1):
            if weights[w] < weights[w+1]:
                temp1=seq[w]
                seq[w]=seq[w+1]
                seq[w+1]=temp1
                temp=weights[w]
                weights[w]=weights[w+1]
                weights[w+1]=temp

    print("Final sequence: ")
    for s in seq:
        print(s, jobs[s])
    return seq

if __name__ == "__main__":
    main()
