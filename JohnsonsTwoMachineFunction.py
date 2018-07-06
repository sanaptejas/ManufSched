# This program is based on Johnson's rule used in OR
# to schedule jobs between two work centers.
# It takes as input the processing time of each job on
# the two work centers.

# Output:
#                Johnson's Rule.
#
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

def main():
    
    print("\n\t\tJohnson's Rule.")

    PT=[ [5,2],[2,6],[1,2],[7,5], [6,6],[3,7],[7,2],[5,1] ]
    JohnsonsRule(PT)

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
    
    print("\nFinal sequence:",first+last)
    
if __name__ == "__main__":
    main()
