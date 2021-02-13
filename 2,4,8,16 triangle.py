def main():
    i = 1
    while i <= 6:
        print(function1(i, 2))
        i += 1
def function1(i, num):
    line = ""
    for j in range(1, i):
        line += str(num) + " "
        num *= 2
    return line
main()
