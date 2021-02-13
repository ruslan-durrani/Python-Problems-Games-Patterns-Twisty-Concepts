S,G = eval(input("Enter Subtotal and Gratuity rate: "))
gratuity = (S*G)/100
subtotal = (S+gratuity)
print("The Gratuity is : ",round(gratuity,2),"\nThe Subtotal is : ",round(subtotal,2))
