
def main():
    machines, jobs, PT, seq=inputPT()
    print("\nMachines: ",machines,"\nJobs:     ", jobs,"\nPT: ", PT,"\nSequence: ", seq)

    print("", end="\n")

def inputPT():
    machines=int(input("Machines: "))
    jobs=    int(input("Jobs:     "))
    print("\n")

    PT=[]
    ## header
    print("    Machines", end="\t")
    for m in range(0, machines):
        print("M/c_{0}".format(m+1), end="\t")
    print("", end="\n")
    ## header border
    print("", end="\t\t")
    for m in range(0, machines):
        print("-----", end="\t")
    ## side column
    print("", end="\n")
    print("Jobs", end="\n")
    print("----")
    ## save input line by line
    for j in range(0, jobs):
        print("Job_{0}".format(j+1),end="\t\t ")
        jobn=list(map(int, input().split()))
        PT.append(jobn)

    sequence=[]
    seqYes=input("Special sequence? [y/N]: ")
    if seqYes=="y":
        print("Sequence: ", end="")
        sequence=list(map(int, input().split()))
    else:
        sequence=list(range(1, jobs+1))

    return machines, jobs, PT, sequence

if __name__=="__main__":
    main()
