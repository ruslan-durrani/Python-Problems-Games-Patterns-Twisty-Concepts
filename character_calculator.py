#charater calculater
def calculator(string):
    count = 0
    for x in string:
        count+=1
    return count

def main():
    string = input("Enter the paragraph :....")
    print("The number of characters in the string is :..",calculator(string))
main()
