#Given Data
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#To Find:........
#We have to find the factor of the First 7 elements

def main():
    T_series = [1,3,6,10,15,21,28]
    
    for x in T_series:
        i=1
        print(format(x,"2d"),":)",end="")
        while i<x+1:
            if x%i==0:
                print(i,end=",")
            i+=1
        print()
main()
