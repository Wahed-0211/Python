
import random 

def signup():
    print("Signup")
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")

    user_data = {
        "name": name,
        "mobile": mobile
    }
    
    print(f"Signup successful! Welcome, {name}.")
    return user_data

def login(user_data):
    generatorotp = random.randint(100000, 999999)

    print(f"Hello {user_data['name']}! Welcome")
    print(f"OTP for login: {generatorotp}")
    
    password = input("Enter the OTP for login: ")
    
    if password == str(generatorotp):
        print("Login successful!")
    else:
        print("Login failed! Invalid OTP.")



def main():
    print("Welcome to the system.")
    
    
    choice = input("Do you have an account? (yes/no): ").strip().lower()
    
    if choice == "no":
        
        user_data = signup()
        print("Now you can login")
        login(user_data)  
    elif choice == "yes":
        
        print("Login page")
        username = input("Username: ") 
        print(f'Hello {username}!')
        login(user_data)
    else:
        print("Invalid choice! Please choose 'yes' or 'no'.")
    
if __name__ == "__main__":
    main()

