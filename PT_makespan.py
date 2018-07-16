import console_input as console

def main():

    machines, jobs, PT, seq=console.inputPT()
    makespan(machines, jobs, PT)

def makespan(machines, jobs, PT):

    maketime=[[0 for m in range(0,machines)] for j in range(0, jobs)]

    ## J1
    for m in range(0, machines):
        maketime[0][m]=maketime[0][m-1]+PT[0][m]
    ## M1
    for j in range(0, jobs):
        maketime[j][0]=maketime[j-1][0]+PT[j][0]

    for j in range(1, jobs):
        #print("JOB: ", j)
        for m in range(0, machines-1):
            #print("  Machine: ", m)
            #print("\tcurrent maketime: {0}\t prev on nxt m/c maketime: {1}".format(maketime[j][m], maketime[j-1][m+1]))
            if maketime[j][m] < maketime[j-1][m+1]:
                maketime[j][m+1]=maketime[j-1][m+1]+PT[j][m+1]
                #print("\t\tnext {0}= prev on nxt m/c {1} + PT nxt m/c {2}".format(maketime[j][m+1],maketime[j-1][m+1],PT[j][m+1]))
            else:
                maketime[j][m+1]=maketime[j][m]+PT[j][m+1]
                #print("\t\tnext {0}= nxt m/c {1} + PT nxt m/c {2}".format(maketime[j][m+1],maketime[j][m],PT[j][m+1]))

    for j in range(0, jobs):
        print(maketime[j])

if __name__=="__main__":
    main()
