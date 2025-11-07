print("---User Registration Program---")
print("Enter your details to register in the application")

# Loop until username is valid
while True:
    username = input("Enter your username: ")
    if len(username) < 3:
        print("❌ Username must contain at least 3 characters. Please try again.")
    elif not username.isalnum():
        print("❌ Username cannot contain special characters or spaces. Use only letters and numbers.")
    
    else:
        break  # exit loop when valid when username length above or equal 3

# Loop until password is valid
while True:
    password = input("Enter your password: ")
    if len(password) < 3:
        print("❌ Password must contain at least 3 characters. Please try again.")
    else:
        break  # exit loop when valid when password length above or equal 3

print(f"✅ You have successfully registered in the application, {username}!")
