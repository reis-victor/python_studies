# Generates a cryptographically secure number
import secrets

# SystemRandom instance from secrets module
number_generator = secrets.SystemRandom()

number = number_generator.randint(1, 10)

print("The random number is", number)

print('Please, guess a number between 1 and 10')

# Asks the user for input and checks if it is an integer number
while True:
    try:
        user_number = int(input('Your number is: '))
        if 10 >= user_number >= 1:
            break
        print('Please, input only integer numbers between 1 and 10!')
    except ValueError:
        print('Please, input only integer numbers between 1 and 10!')

while number != user_number:
    try:
        user_number = int(input('Please, select another number!'))
        if not 10 >= user_number >= 1:
            print('Please, input only integer numbers between 1 and 10!')
            continue
    except ValueError:
        print('Please, input only integer numbers between 1 and 10!')
        continue
    if user_number > number:
        print('Too high!')
    elif user_number < number:
        print('Too low!')
    else:
        print('Awesome! The number is correct!')
        break
