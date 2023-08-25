email = input("what is your email?").strip()

username, domain = email.split("@")

if username and domain.endswith("edu"):
    print("valid email")
else:
    print("email not valid")

    #Work through regular expressions