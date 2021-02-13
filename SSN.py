def main():
    ssn = str(input("Enter SSN code: "))
    Three = ssn[3]
    Six = ssn[-5]
    L = ssn[0:3]
    E = ssn[7:]
    if Three == "-" and Six == "-" and len(L) == 3 and len(E) == 4:
        print("Correct SSN")
    else:
        print("Incorrect SSN")
main()
