secret_film_character = 'andor'

counter = 0
n_trail = 3
while  counter < n_trail:
    guess = input("Who is the secret character ?").lower()
    counter += 1
    if secret_film_character == guess:
        print("you won !!!!")
        break
else:
    print("It is gone")
