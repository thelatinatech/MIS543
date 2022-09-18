# While loop with User Input
while True:
    yes_no = input("Do you want to continue? Yes or No?: ")

    if yes_no.lower() == 'yes' or yes_no.lower() == 'y':
        print("Okay!")
        continue

    elif yes_no.lower() == 'no' or yes_no.lower() == 'n':
        print("Done!")
        break

    else:
        print("Type either 'yes' or 'no'. ")
        continue
