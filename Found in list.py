#FINDING DATA
N_list = []
for x in range(5):
    N_list.append(int(input("Enter data :..")))
print()
find = int(input("ENTER THE NUMBER YOU WANNA FIND:>>>>"))
found = find in N_list
if found:
    print("YES FOUND it is located in the index number ",N_list.index(find))
else:
    print("NO SORRY I COULDNT GET IT ")





