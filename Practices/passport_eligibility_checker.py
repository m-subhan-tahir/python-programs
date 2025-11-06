print("=== Passport Eligibility Checker (Pakistan) ===")

citizenship = input("Are you a Pakistani citizen? (yes/no): ").strip().lower()

if citizenship != "yes":
    print("❌ You are not eligible — only Pakistani citizens can apply for a passport.")
else:
    age = int(input("Enter your age: "))

    if age >= 18:
        has_cnic = input("Do you have a valid CNIC or B-Form? (yes/no): ").strip().lower()
        if has_cnic != "yes":
            print("❌ You need a valid CNIC or B-Form to apply for a passport.")
        else:
            print("✅ You are eligible for an adult passport.")
    elif 0 < age < 18:
        print("✅ You are eligible for a child passport (with parent/guardian consent).")

    else:
        print("❌ Invalid age entered.")