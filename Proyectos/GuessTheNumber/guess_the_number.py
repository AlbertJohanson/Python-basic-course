import random

def run():

    number = random.randint(1, 100)

    while True:
        guess = int(input('Try to guess the number: '))

        if guess == number:
            print('You won!')
            break
        elif guess > number:
            print('Your guess is too high')
        else:
            print('Your guess is too low') 
    

if __name__ == '__main__':
    run()