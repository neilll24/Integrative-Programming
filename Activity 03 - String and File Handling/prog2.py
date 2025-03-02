# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first name and last name
full_name = first_name + " " + last_name

# Display the full name in upper and lower case
full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

# Count and display the length of the full name
full_name_length = len(full_name)

# Display output
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", full_name_upper)
print("Full Name (Lower Case):", full_name_lower)
print("Length of Full Name:", full_name_length)
