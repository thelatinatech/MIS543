# while loop with user input
while True:
    try:
        number = int(input("Please enter an integer: "))
        print(f"Success!")
        break
    except ValueError:
        print("Error - not an integer!")
        continue

# This appends the user_input to the numbers.txt file
numbers_file = open("numbers.txt", "a")
numbers_file.write(f"\n{number}")
numbers_file.close()