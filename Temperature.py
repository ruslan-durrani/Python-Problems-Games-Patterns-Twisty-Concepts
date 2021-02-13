'''
Write a Python code to accept temperature value from user (in centigrade)
and display an appropriate message as below. 
 FREEZING if temperature in less than 0 COLD if temperature
 is between 0 to 15 WARM if temperature is between 16 to 30
 '''
User = eval(input("Enter temperature in Centigrates:.."))
if User < 0 :
    print("FREEZING")
elif 0<User<16:
    print("COLD")
elif 15<User<32:
    print("WARM")
elif 31<User<41:
    print("HOT")
else:
    print("VERY HOT")
