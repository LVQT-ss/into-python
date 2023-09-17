def main():
    print("welcome to the email slicer ")
    print("")

    email_input = input("input your email address :")

    (username,domain)= email_input.split("@")
    (domain,extension) = domain.split(".")

    print("usernam :",username)
    print("domain :",domain)
    print("extension:",extension)
while True:
    main()