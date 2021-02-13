#final 3 Question 1

N = input("Enter number separated by space: ").split()
S = []
string = ""
for x in N:
    S.append(int(x[0]))
leng = len(S)
for j in range(leng):
    s = max(S)
    for k in N:
        if str(s)== k[0]:
            string += k
    S.remove(s)
            
print(string)
print(N)

#final 3 question 2
set1 = input("Enter : ").split()
set1 = list(int(x) for x in set1)
new_set = []
L = len(set1)
u = 0
while u != L:
    for x in range(len(set1)):
        if x == len(set1)-1:
            x = -1
        j = abs(set1[x]-set1[x+1])
        new_set.append(j)
    print(new_set)
    set1 = new_set
    new_set = []
    u +=1

#final 3 question 3
def union(s1,s2):
    res = list(s1) + list(s2)
    return set(res)
def main():
    set1 = input("Set1: ").split()
    set1 = set(int(x) for x in set1)
    
    set2 = input("Set2: ").split()
    set2 = set(int(x) for x in set2)
    
    print("The union of sets is : ",union(set1,set2))
main()
# final 3 question 4
def encryptMessage(String):
    codes = { '1' : '[', '2' : '_', '3' : ')', '4' : '}', '5' : ']', '6' : '{' }
    L = [x for x in String]
    reTurn = ""
    for x in L:
        if x in codes:
            reTurn += codes[x]
    return reTurn
    
def main():
    inp = input("Enter string 1-6: ")
    print("Encrypted:",encryptMessage(inp))
    
main()

#final 2 question 4
def decryptMessage(String):
    dcodes = { '%' : 'A', '9' : 'a', '@' : 'B', '#' : 'b', '.' : 'C', ',' : 'c' }
    L = [x for x in String]
    reTurn = ""
    for x in L:
        if x in dcodes.keys():
            reTurn += dcodes.get(x)
    return reTurn
    
def main():
    inp = input("Enter string: ")
    print("Encrypted:",decryptMessage(inp))
    
main()

#final 2 Question 3
def intersection(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    res = []
    for x in range(len(s1)):
        if s1[x] in s2:
            res.append(s1[x])
    return set(res)
    return set(res)
def main():
    set1 = input("Set1: ").split()
    set1 = set(int(x) for x in set1)
    
    set2 = input("Set2: ").split()
    set2 = set(int(x) for x in set2)
    
    print("The intersection of sets is : ",intersection(set1,set2))
main()
 




#final 2 Question 3
def difference(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    #res = []
    for x in range(len(s2)):
        if s2[x] in s1:
            s1.remove(s1[x])
    return set(s1)
def main():
    set1 = input("Set1: ").split()
    set1 = set(int(x) for x in set1)
    
    set2 = input("Set2: ").split()
    set2 = set(int(x) for x in set2)
    
    print("The difference of sets is : ",difference(set1,set2))
main()
 















