name = input("What is your name ?")
N_cha_name = len(name) 

if N_cha_name < 3:
    print("need at least 3 characters long")
elif N_cha_name > 5:
    print("5 characters max")
else:
    print("name looks good")

'''
input_currency = input ("Enter currency to convert :")
splited_input = input_currency.lower().split()

if splited_input[-1] == "euros": 
    eu_to_dollar = 1.09 * int(splited_input[0])
    print(f"{eu_to_dollar}" + " Euros")
elif splited_input[-1] == "dollars":
    dollar_to_eu = 0.92 * int(splited_input[0])
    print(f"{dollar_to_eu}" + " Dollars")
else:
    print("You need to enter a number and a symbol in plurial")
'''