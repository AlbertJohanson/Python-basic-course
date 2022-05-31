# def print__message():
#     print("Special Message")
#     print("Im learning to use functions")

# print__message()
# print__message()
# print__message()

def print_message(option):
    print("Hi")
    print("How are you?")
    print("You choose the option " + option)
    print("Good bye")


option = input("Choose a option (1, 2, 3): ")

if(option == '1'):
    print_message(option)
elif(option == '2'):
    print_message(option)
elif(option == '3'):
    print_message(option)
else:
    print("Please choose a valid option")



