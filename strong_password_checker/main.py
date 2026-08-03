def is_strong_password(password):
    pl = len(password)
    pass_len = pl >= 8 and pl <= 20
    lower_case = False
    upper_case = False
    specials = "!@#$%^&*?"
    number = False
    is_special = False
    is_digit = False
    no_space = True
    identical_char = False
    first_char = False

    i = 0
    fc = password[0]

    if "a" <= fc <= "z" or "A" <= fc <= "Z":
        first_char = True
    
    for ch in password:
        if "a" <= ch <= "z":
            lower_case = True
        elif "A" <= ch <= "Z":
            upper_case = True
        elif ch in specials:
            is_special = True
        elif ch.isdigit():
            is_digit = True
        elif ch == " ":
            no_space = False
            print("there's a space")

    max_i = pl - 3
    print(max_i)
    
    while i < max_i and pass_len:
        if password[i] == password[i + 1] and password[i + 1] == password[i + 2]:
            print("match")
            identical_char = True
        i += 1
            
    if pass_len and first_char and lower_case and upper_case and is_special and is_digit and no_space and not identical_char:
        print(True)
        strong_pass = True
    else:
        print(False)
        strong_pass = False

    return strong_pass
