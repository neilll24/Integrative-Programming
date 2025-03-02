# Open the file in read mode
try:
    with open("students.txt", "r") as file:
        # Read the contents of the file
        student_data = file.read()
        
        # Display the student information
        print("Reading Student Information:\n")
        print(student_data)

except FileNotFoundError:
    print("Error: 'students.txt' not found. Please ensure the file exists before reading.")
