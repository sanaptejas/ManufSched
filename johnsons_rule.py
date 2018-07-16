import console_input as console

def main():

    print("Johnson's rule works only for TWO workstations.")

    machines, jobs, PT, seq=console.inputPT()
    algo(machines, jobs, PT)

def algo(machines, jobs, PT):

    first=[]
    indexfirst=[]
    last=[]
    indexlast=[]

    print("",end="\n\n")
    for j in range(0, jobs):
        if PT[j][1] > PT[j][0]:
            first.append(PT[j])
            indexfirst.append(j+1)
        else:
            last.append(PT[j])
            indexlast.append(j+1)

    for n in range(0, jobs):
        for j in range(1, len(first)):
            if first[j][0] <= first[j-1][0]:
               temp=first[j]
               first[j]=first[j-1]
               first[j-1]=temp
               temp=indexfirst[j]
               indexfirst[j]=indexfirst[j-1]
               indexfirst[j-1]=temp

        for j in range(1, len(last)):
            if last[j][1] >= last[j-1][1]:
               temp=last[j]
               last[j]=last[j-1]
               last[j-1]=temp
               temp=indexlast[j]
               indexlast[j]=indexlast[j-1]
               indexlast[j-1]=temp

    final=first+last
    indexfinal=indexfirst+indexlast

    for j in range(0, jobs):
        print(indexfinal[j], final[j])

if __name__=="__main__":
    main()
