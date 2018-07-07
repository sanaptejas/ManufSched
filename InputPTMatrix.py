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
# 
# [[16, 18, 12], [14, 10, 11], [13, 20, 15], [19, 15, 19], [15, 16, 16]]

def main():
    machines=int(input("Machines: "))
    items=int(input("Items: "))
    
    take_input(machines, items)

def take_input(machines, items):
    PT=[]
    print("\t ", end=" ")
    for m in range(0, machines):
        print("M/c {0} |".format(m+1), end=" ")
    
    print()
    for m in range(0, machines):
        print("------------", end="")
    
    print()
    for i in range(0,items):
        print("Job{0}".format(i+1), end="\t| ")
        a=list(map(int,input().split()))
        PT.append(a)
    print(PT, end="\n")
    return PT 

if __name__=="__main__":
    main()
