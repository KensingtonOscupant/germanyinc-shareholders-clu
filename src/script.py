import csv
import sys
import termios
import tty

def getch():
    """Get a single character from the user without the need to press enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Open the CSV file and read the data
with open("data/sample_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Initialize a variable to store the next unique ID
next_id = 1

# Print a welcome message
print("Welcome to the company matching utility!")
print("Press 'n' if the two strings are not the same company.")
print("Press '1' if the first string is the correct spelling.")
print("Press '2' if the second string is the correct spelling.")
print("Press 'b' to go back to the previous question.")
print("Press 'q' to quit the utility.")

# Keep track of the current question index
current_index = 0

# Find the first empty company_id
for i, row in enumerate(data):
    if row["company_id"] == "":
        current_index = i
        break

while current_index < len(data):
    row = data[current_index]
    target_string = row["target_string"]
    matched_string = row["matched_string"]
    company_id = row.get("company_id", "")

    # Print a newline for spacing
    print("\n")

    # Print the strings and ask the user for input
    print("Target:", target_string)
    print("Matched:", matched_string)
    print("Company ID:", company_id)
    print("Are these the same company? (n/1/2/b/q)")

    while True:
        user_input = getch().lower()
        if user_input in ["n", "1", "2"]:
            break
        elif user_input == "b":
            if current_index > 0:
                current_index -= 2
                break
            else:
                print("Cannot go back, already at the first question.")
        elif user_input == "q":
            sys.exit("Exit the script")
        else:
            print("Invalid input. Please enter 'n', '1', '2', 'b' or 'q'")

    # Update the company_id based on the user input
    if user_input == "n":
        row["company_id"] = "0"
    elif user_input in ["1", "2"]:
        row["company_id"] = str(next_id)
        next_id += 1

    current_index += 1
    # Write the updated data to the CSV file
    with open("data/sample_data.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("Data written to file.")
