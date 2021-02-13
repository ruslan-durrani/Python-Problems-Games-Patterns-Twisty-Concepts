#standard deviation
import math
def summation(LIST):
    sum = 0
    for d in LIST:
        sum+=d
    return(sum/(len(LIST)))

def STD(Lust,avg):
    sumtion = 0
    for x in Lust :
        sumtion+=(x-avg)**2
    sumtion = math.sqrt(sumtion/(len(Lust)-1))
    return sumtion
        
def main():
    i = 1
    Data = input("Enter data with spaces: ").split()
    Data = [eval(x) for x in Data]
    avg = summation(Data)
    devi = STD(Data,avg)
    print(avg)
    print(devi)
main()
