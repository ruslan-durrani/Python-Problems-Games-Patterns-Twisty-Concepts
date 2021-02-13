w = eval(input("Weight in pounds: "))
i = eval(input("Height in inches"))
k = w*0.45359237
h = i*0.0254
BMI = k/(h**2)
if BMI <18.5:
    print("UNder")
elif BMI < 25:
    print("NORMAL")
elif BMI < 30:
    print("Overweight")
else:
    print("OBESE")
    
