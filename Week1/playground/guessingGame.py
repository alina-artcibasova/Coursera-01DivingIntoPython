import random

number = random.randint(0, 101)

while True:
    answer = input('Guess the number: ')
    if answer == "" or answer == "exit":
        print("Exiting the program")
        break
    
    if not answer.isdigit():
        print("Enter correct number!")
        continue
    
    answer = int(answer)
    
    if answer == number:
        print('Absolutely correct!')
        break
    
    elif answer < number:
        print('The number is bigger')
    else:
        print('The number is smaller')
