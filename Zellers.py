def zeller(day, month, year):
        
    if(month == 1):
        A = 11
        myy = year-1
    elif(month == 2):
        A = 12
        myy = year-1
    elif(month == 3):
        A = 1
        myy = year
    elif(month == 4):
        A = 2
        myy = year
    elif(month == 5):
        A = 3
        myy = year
    elif(month == 6):
        A = 4
        myy = year
    elif(month == 7):
        A = 5
        myy = year
    elif(month == 8):
        A = 6
        myy = year
    elif(month == 9):
        A = 7
        myy = year
    elif(month == 10):
        A = 8
        myy = year
    elif(month == 11):
        A = 9
        myy = year
    elif(month == 12):
        A = 10
        myy = year
 
    yOcList = list(str(myy))
    yearOfCentury = yOcList[2]+yOcList[3]
 
    CenturyList = list(str(myy))
    Century = yOcList[0]+yOcList[1]
 
    B = day
    C = int(yearOfCentury)
    D = int(Century)
 
    W = (13*int(A) -1)/5
    X = int(C)/4
    Y = int(D)/4
    Z = int(W) + int(X) + int(Y) + int(B) + int(C) - 2*int(D)
    R = int(Z)%7
    
 
    if(int(R)==0):
        return "Sunday"
    elif(int(R)==1):
        return "Monday"
    elif(int(R)==2):
        return "Tuesday"
    elif(int(R)==3):
        return "Wednesday"
    elif(int(R)==4):
        return "Thursday"
    elif(int(R)==5):
        return "Friday"
    elif(int(R)==6):
        return "Saturday"
def main():
    Year = int(input("Shayesta:..Enter the Birth YEAR you were born:.."))
    Month = int(input("Shayesta:..ENTER THE BIRTH MONTH :...."))
    Date = int(input("Shayesta:..ENTER THE Birth DATE OF month:...."))
    day = zeller(Date,Month,Year)
    print("Dear shayesta...The day you were born was :.....",day)
main()
