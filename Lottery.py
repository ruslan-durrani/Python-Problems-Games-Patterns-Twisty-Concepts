'''
import random
Lottery = random.randint(10,99)
D2 = Lottery%10
D1 = Lottery//10
User = int(input("Enter your lottery Guess number: "))
User1 =User//10
User2 = User%10
print("The lottery number is : ",Lottery)
if Lottery == User:
    print("Exact match found. You won 5000$")
elif User1==D2 and User2==D1:
    print("Two Matches found. You won 2000$")
elif User1==D1 or User1==D2 or User2==D1 or User2 == D2:
    print("One match found. You won 1000$")
else:
    print("No match found.\nBetter luck next time.")
'''
import random
Lottery = random.randint(101,999)
D3 = Lottery%10
D = Lottery//10
D2 = D%10
D1 = D//10
User = int(input("Enter your lottery Guess number: "))
User3 = User%10
User_ = User//10
User2 =User_ % 10
User1 = User_//10
print(Lottery)
print("The lottery number is : ",Lottery)
if Lottery == User:
    print("Exact match found. You won 5000$")
elif (User1==D3 or User1==D2 or User1 == D1) and (User2==D3 or User2==D2 or User2 == D1) and (User3==D3 or User3==D2 or User3 == D1):
    print("Three Matches found. You won 2000$")
elif User1==D1 or User1==D2 or User1 == D3 or User2==D1 or User2 == D3 or User2 == D2 or User3 == D3 or User3 == D2 or User3 == D1:
    print("One match found. You won 1000$")
else:
    print("No match found.\nBetter luck next time.")
