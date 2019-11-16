# Generates a cryptographically secure number
import secrets

# SystemRandom instance from secrets module
number_generator = secrets.SystemRandom()

number = number_generator.randint(1, 10)

# The following code is used to print the generated number: print("The random number is", number)

print("Please, guess a number between 1 and 10")

# Asks the user for input and checks if it is an integer number
while True:
    user_number = input("Your number is: ")
    try:
      user_number = int(user_number)
      break
    except ValueError:
      print("Please, input only integer numbers between 1 and 10!")
      continue

while number != user_number:
    print ("Please, select another number!")
    user_number = int(input())
    if user_number > number:
      print("Too high!")
    elif user_number < number:
      print("Too low!")
    else:
      print("Awesome! The number is correct!")
      break