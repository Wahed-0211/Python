
import random 
generatorotp=random.randint(000000, 1000000)
Mobilenumber=input("Mobilenumber:")
print('Mobilenumber:', Mobilenumber)
print('OTP for login', generatorotp)
password=input("Enter the otp for login:")
if password==str(generatorotp):
    print('Login successful')
else:
    password!=str(generatorotp)    
    print('Login Failed')