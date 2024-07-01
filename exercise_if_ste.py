house = 1000000

#good_credit = True
#excelent_credit = False

#good_credit = False
#excelent_credit = True

good_credit = False
excelent_credit = False

if good_credit:
    print(f"As you are a good borrower the total price is {house * 0.9}" )

elif excelent_credit:
    print(f"As you are a excellent  borrower the total price is {house * 0.8}" )
    
else:
    print("The total price is : ", house)