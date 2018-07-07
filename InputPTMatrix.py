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
