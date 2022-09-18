while True:
    try:
        number = int(input("Please enter an integer: "))
        print(f"Success!")
        break
    except ValueError:
        print("Error - not an integer!")
        continue

