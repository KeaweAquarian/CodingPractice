email = input("what is your email?").strip()

if "@" in email:
    print("valid email")
else:
    print("email not valid")