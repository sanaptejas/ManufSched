# This program calculates for a given sequence of
# jobs the total makespan.

# Output:
# 1 [10, 6]
# 2 [6, 12]
# 3 [8, 9]
# 4 [8, 10]
# 5 [12, 5]
# 
# [[10, 16], [0, 0], [0, 0], [0, 0], [0, 0]]
# [[10, 16], [16, 28], [0, 0], [0, 0], [0, 0]]
# [[10, 16], [16, 28], [24, 37], [0, 0], [0, 0]]
# [[10, 16], [16, 28], [24, 37], [32, 47], [0, 0]]
# [[10, 16], [16, 28], [24, 37], [32, 47], [44, 52]]
#
#Makespan:  52

#PT=[ [5,2],[2,6],[1,2],[7,5], [6,6],[3,7],[7,2],[5,1] ]
PT=[[10,6],[6,12],[8,9],[8,10],[12,5]]

items=len(PT)
machines=len(PT[0])

jobs = dict((key, PT[key]) for key in range(0, items) )

makespan=[[0,0] for x in range(0,items)]

for j in range(0,items):
    print(j+1, jobs[j])

print()

for j in range(0,items):
        makespan[j][0]=makespan[j-1][0]+PT[j][0]

        if makespan[j][0] < makespan[j-1][1]:
            makespan[j][1]=makespan[j-1][1]+PT[j][1]
        else:
            makespan[j][1]=makespan[j][0]+PT[j][1]

        print(makespan)

print("\nMakespan: ",makespan[items-1][machines-1])
