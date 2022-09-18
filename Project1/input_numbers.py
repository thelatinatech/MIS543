def user_input():
    try:
        number = int(input("Please enter an integer: "))
        print(f"Success! Number is {number}")
        numbers_func(number)
        question_func()

    except ValueError:
        print("Error - not an integer!")
        user_input()

def question_func():
    question = input("Do you want to continue? Enter either 'Yes' or 'No'. ")

    if question.lower() == "yes" or question.lower() == "y":
        user_input()
    elif question.lower() == "no" or question.lower() == "n":
        print("Okay, done!")
        return 0
    else:
        print("Please enter either 'Yes' or 'No'.")
        question_func()


def numbers_func(number):
    # This appends the user_input to the numbers.txt file
    numbers_file = open("numbers.txt", "a")
    numbers_file.write(f"\n{number}")
    numbers_file.close()


user_input()