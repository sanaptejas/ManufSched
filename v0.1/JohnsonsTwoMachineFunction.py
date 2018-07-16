import InputPTMatrix as PTmatrix
import MeasureMakespanFunction as makespan

# This program is based on Johnson's rule used in OR
# to schedule jobs between two work centers.
# It takes as input the processing time of each job on
# the two work centers.
# 
# Output: 
# 		Johnson's Rule.
# Items: 8
# 	  M/c 1 | M/c 2 | 
# ------------------------
# Job1	| 5	2
# Job2	| 2	6
# Job3	| 1	2
# Job4	| 7	5
# Job5	| 6	6
# Job6	| 3	7
# Job7	| 7	2
# Job8	| 5	1
# [[5, 2], [2, 6], [1, 2], [7, 5], [6, 6], [3, 7], [7, 2], [5, 1]]
# 1 [5, 2]
# 2 [2, 6]
# 3 [1, 2]
# 4 [7, 5]
# 5 [6, 6]
# 6 [3, 7]
# 7 [7, 2]
# 8 [5, 1]
# 
# Jobs that will go first: [2, 3, 6]
# Jobs that will go last: [1, 4, 5, 7, 8]
# 
# Jobs going first arranged in ascending order: [3, 2, 6]
# Jobs going last arranged in descneding order: [5, 4, 7, 1, 8]
# 
# Final sequence: [3, 2, 6, 5, 4, 7, 1, 8]
# Normal makespan: 
# [[ 5.  7.]
#  [ 7. 13.]
#  [ 8. 10.]
#  [15. 20.]
#  [21. 27.]
#  [24. 31.]
#  [31. 33.]
#  [36. 37.]]
# Optimal makespan: 
# PT matrix according to sequence
# 3 [1, 2]
# 2 [2, 6]
# 6 [3, 7]
# 5 [6, 6]
# 4 [7, 5]
# 7 [7, 2]
# 1 [5, 2]
# 8 [5, 1]
# Makespan
# [[ 1.  3.]
#  [ 3.  9.]
#  [ 6. 13.]
#  [12. 18.]
#  [19. 24.]
#  [26. 28.]
#  [31. 33.]
#  [36. 37.]]


def main():
    print("NOTE: Enter no. of machines as 2.")
    print("\n\t\tJohnson's Rule.")

    #PT=[ [5,2],[2,6],[1,2],[7,5], [6,6],[3,7],[7,2],[5,1] ]
    PT, items, machines=PTmatrix.take_input() 
    machines=2
    seq=JohnsonsRule(PT)
    print("Normal makespan: ")
    makespan.plain_makespan(PT, items, machines)
    print("Optimal makespan: ")
    makespan.seq_makespan(PT, items, machines, seq)

def JohnsonsRule(PT):
 
    n=len(PT)
    jobs=dict((key+1, PT[key]) for key in range(0,n))
    
    first=[]
    last=[]
    
    
    for j in range(1, n+1):
        print(j, jobs[j])
    
    
    for j in range(1,n+1):
        if jobs[j][0] < jobs[j][1]:
            first.append(j)
        else:
            last.append(j)
    
    print("\nJobs that will go first:",first)
    print("Jobs that will go last:",last)
    
    for k in range(0, len(first)):
        for j in range(0,len(first)-1):
            if jobs[first[j]][0] >= jobs[first[j+1]][0]:
                temp=first[j]
                first[j]=first[j+1]
                first[j+1]=temp
    
    print("\nJobs going first arranged in ascending order:",first)
    
    for k in range(0,len(last)):
        for j in range(0,len(last)-1):
            if jobs[last[j]][1] <=  jobs[last[j+1]][1]:
                temp=last[j]
                last[j]=last[j+1]
                last[j+1]=temp
    
    #last = list( reversed(last)  )
    print("Jobs going last arranged in descneding order:",last)
    final=first+last
    print("\nFinal sequence:", final)
    return final
    
if __name__ == "__main__":
    main()
