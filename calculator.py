from os import system

system('cls')

while True:
    print("Write your math operation or (x) to exit: ")
    user_input =input()
    if user_input == 'x':
        print("Thanks for using our app!")
        break

    else:
        print("Answer:",eval(user_input))
 