name = input('What is your name ? ')
fav_color = input('What is your favorite color ? ')
print('Hi ' + name + '. It looks like you love ' + fav_color )
print('Thats cool. Lets move to next step')
print(' ')

birth_year = int(input('What year were you born ? '))
birth_city = input('Where were you born ? ')
age = (2024 - birth_year)
print('Hi, ' + name + ' it looks like you are ', age , ' and you were born in ' + birth_city )
print(' ')
print("Thats cool. Let's Convert your weight into Kg")


weight = int(input("What is your weight in lb ? "))
weight_kg = 0.45 * weight
print("Wow !", name, "it looks like you weight ", weight_kg,'Kg' )
