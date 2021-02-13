#def
def hi(name):
    
    if ("ALI" or "nasir") in name:
        print("HI ",name)
    else:
        print("YOUR ARE NOT OF THIS CLASS")
    
    
def main():
    for x in range(2):
        name = input("ENTER YOUR NAME :>>>")
        hi(name)
main()

