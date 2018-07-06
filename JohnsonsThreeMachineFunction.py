# This program shows the special case of
# Johnson's Rule in which the optimal queue
# for three machines is calculated based on
# criteria the maximum time on machine three
# should be less than or equal to the
# minimum time on machine 1 and 3.

# Output:
#                    Johnson's Three Machine Rule.
# 
# 1 [4, 4, 6]
# 2 [9, 5, 9]
# 3 [8, 3, 11]
# 4 [6, 2, 8]
# 5 [3, 6, 7]
# 
# Minimum on Machine 1: 3
# Maximum on Machine 2: 6
# Minimum on Machine 3: 6
# 
# Combined PT matrix: [[8, 10], [14, 14], [11, 14], [8, 10], [9, 13]]
# 
# 1 [8, 10]
# 2 [14, 14]
# 3 [11, 14]
# 4 [8, 10]
# 5 [9, 13]
# 
# Jobs that will go first: [1, 3, 4, 5]
# Jobs that will go last: [2]
# 
# Jobs going first arranged in ascending order: [4, 1, 5, 3]
# Jobs going last arranged in descneding order: [2]
# 
# Final sequence: [4, 1, 5, 3, 2]
import JohnsonsTwoMachineFunction as JR2

def main():

    print("\n\t\tJohnson's Three Machine Rule.\n")
    PT=[ [4,4,6], [9,5,9], [8,3,11], [6,2,8], [3,6,7] ]
    criteria(PT)

def criteria(PT):

    ## prepare PT for individual machines
    machine1=[]
    machine2=[]
    machine3=[]
    n=len(PT)
    
    for j in range(0, n):
        print(j+1, PT[j])
        machine1.append(PT[j][0])
        machine2.append(PT[j][1])
        machine3.append(PT[j][2])
    
    ## find maximum on machine 2 and minimum on machine 1 and 3
    min1=min(machine1)
    max2=max(machine2)
    min3=min(machine3)
    
    print("\nMinimum on Machine 1: {0}\nMaximum on Machine 2: {1}\nMinimum on Machine 3: {2}".format(min(machine1),max(machine2),min(machine3)))
    
    ## check if PT matrix satisfies Johnson's criteria
    if max2 <= min1:
        fictiousMachines(machine1, machine2, machine3, n)
    elif max2 <= min3:
        fictiousMachines(machine1, machine2, machine3, n)
    else:
        quit()

def fictiousMachines(machine1, machine2, machine3, n):

    ## add machine 1 and 2 and machine 2 and 3 PT
    comb12=[]
    comb23=[]
    
    for j in range(0, n):
        comb12.append(machine1[j]+machine2[j])
        comb23.append(machine2[j]+machine3[j])
    
    #print("\nCombined machine 1 and machine 2 time: ",comb12,"\nCombined machine 2 and machine 3 time: ",comb23)
    
    ## prepare PT matrix for combined times
    combinedPT=[[0,0] for n in range(0, n)]
    
    for j in range(0, n):
        combinedPT[j][0]=comb12[j]
        combinedPT[j][1]=comb23[j]
    
    print("\nCombined PT matrix:", combinedPT)
    print()

    JR2.JohnsonsRule(combinedPT)

if __name__ == "__main__":
    main()
