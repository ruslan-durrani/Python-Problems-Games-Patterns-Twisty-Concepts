def isAnagram(k1,k2):
    S1 = [ord(x) for x in k1] #Store Ascii characters 
    S2 = [ord(j) for j in k2] #Store Ascii characters 
    S1.sort() # Sorting 
    S2.sort() #sorting
    if S1==S2:
        return True
    else:
        return False     
def main():
    s1=input("Enter elements of list1: ").lower() #{shayesta)
    s2=input("Enter elements of list2: ").lower() #{shayesta)
    
    if isAnagram(s1,s2)==True:  #Function call
        print("The two words are anagrams")
    else:
        print("The two words are not anagrams")
main()
