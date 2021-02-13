#Method 1
def main():
    S = input("Enter String: ")
    N = ""
    for x in range(len(S)-1,-1,-1):
        N += S[x]
    if N == S:
        print("Palindrome")
    else:
        print("NON")
main()


#Method 2
def main():
    G = True
    S = input("Enter String: ")
    L = 0
    H = len(S)-1
    while L<H:
        if S[L] != S[H]:
            G = False
            break
        L += 1
        H -=1
    if G == True:
        print("Palindrome")
    else:
        print("Non Palindrome")

    
main()
