def get_valid_int():
    """Prompt the user for an integer input until a valid integer is entered."""
    while True:
        try:
            # Try to convert the user input into an integer
            return int(input("Please enter an integer: "))
        except ValueError:
            # If a ValueError is raised, print an error message
            print("That's not a valid integer. Please try again.")

def main():
    total = 0
    for _ in range(5):
        total += get_valid_int()
    print(f"The sum of the entered values is: {total}")

if __name__ == "__main__":
    main()
