# This program is based on Johnson's rule used in OR
# to schedule jobs between two work centers.
# It takes as input the processing time of each on the
# two work centers.

# Output:
# 1 [5, 2]
# 2 [2, 6]
# 3 [1, 2]
# 4 [7, 5]
# 5 [6, 6]
# 6 [3, 7]
# 7 [7, 2]
# 8 [5, 1]
# Old Job1:  [2, 3, 6]
# New Job1:  [3, 2, 6]
# Old Job2:  [1, 4, 5, 7, 8]
# New Job2:  [8, 7, 1, 4, 5]
# Final sequence:  [3, 2, 6, 8, 7, 1, 4, 5]

import random

#PT=[random.sample(range(1,100),2) for x in range(0,10)]
PT=[ [5,2],[2,6],[1,2],[7,5], [6,6],[3,7],[7,2],[5,1] ]

n=len(PT)
jobs=dict((key+1, PT[key]) for key in range(0,n))

job1=[]
job2=[]

for j in range(1, n+1):
    print(j, jobs[j])


for j in range(1,n+1):
    if jobs[j][0] < jobs[j][1]:
        job1.append(j)
    else:
        job2.append(j)

print("Old Job1: ",job1)

for k in range(0, len(job1)):
    for j in range(0,len(job1)-1):
        if jobs[job1[j]][0] > jobs[job1[j+1]][0]:
            temp=job1[j]
            job1[j]=job1[j+1]
            job1[j+1]=temp

print("New Job1: ",job1)

print("Old Job2: ",job2)

for k in range(0,len(job2)):
    for j in range(0,len(job2)-1):
        if jobs[job2[j]][1] <  jobs[job2[j+1]][1]:
            temp=job2[j]
            job2[j]=job2[j+1]
            job2[j+1]=temp

job2 = list( reversed(job2)  )
print("New Job2: ",job2)

print("Final sequence: ",job1+job2)
