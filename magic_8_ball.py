import secrets
import sys

number_generator = secrets.SystemRandom()


def game():
    input('What is your question?:     ')
    ball_number = ('It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it',
                   'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
                   'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                   'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no',
                   'Outlook not so good', 'Very doubtful')
    number = number_generator.randint(1, 20)
    print(ball_number[number])
    end()


def end():
    question = input('Do you have any other questions?:     ')
    if question == 'YES' or question == 'yes' or question == 'y':
        game()
    elif question == 'NO' or question == 'no' or question == 'n':
        print('See you soon!')
        sys.exit()
    else:
        print('Yes or no?')
        end()


game()
