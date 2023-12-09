def process_numbers(filename):
    try:
        # Read numbers from the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Check if there are at least two numbers
        if len(lines) >= 2:
            # Get the first two numbers
            first_number = float(lines[0].strip())
            second_number = float(lines[1].strip())

            # Handle ZeroDivisionError
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                return

            # Perform the division and store the result in memory
            temp = first_number / second_number
            print("Result of division:", temp)

            # Add 1 to temp and append it on a new line in the file
            with open(filename, 'a') as file:
                temp+=1
                file.seek(0,2)
                file.write(f"\n{temp}")

        else:
            print(f"Error: Insufficient numbers in '{filename}'. Need at least two.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    filename = "numbers.txt"
    process_numbers(filename)
