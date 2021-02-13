#unique word in Paragraph string
Para = input("Enetr a pharagraph").lower()
if " " in Para:
    Para.replace(" ","")
Unique = []
for x in Para:
    if x in Unique:
        pass
    else:
        Unique.append(x)
L = len(Unique)
print("The unique letter in Paragraph is : ",L)
