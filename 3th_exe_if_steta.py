name = input("What is your name ?")
N_cha_name = len(name) 

if N_cha_name < 3:
    print("need at least 3 characters long")
elif N_cha_name > 5:
    print("5 characters max")
else:
    print("name looks good")
