#Palindromoeoji
def palindrome(DATA):
    return True if DATA[::-1]==DATA else False
    
def main():
    name = input("ENTER A NAME TO FIND ITS PALINDROMICITY:>>>").upper()
    isP = palindrome(name)
    if isP :
        print("Yes the name is a palindrome :>>>>")
    else:
        print("NON PALINDROME:>>>>")
main()
