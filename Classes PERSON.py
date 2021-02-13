class PERSON():
   def __init__(self,NAME,AGE):
       self.NAME = NAME
       self.AGE = AGE
N = input("Enter name:...")
A = int(input("Enter Age:..."))
VARIABLE = PERSON(N,A)
print(VARIABLE.NAME , VARIABLE.AGE)
