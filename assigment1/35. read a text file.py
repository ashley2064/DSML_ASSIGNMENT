
def analyze_and_write(time, time1):
    letters = 0
    digits = 0
    others = 0

    with open(time, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    letters += 1
                elif char.isdigit():
                    digits += 1
                elif not char.isspace():
                    others += 1

    with open(time1, 'w') as file:
        file.write(f"Number of letters: {letters}\n")
        file.write(f"Number of digits: {digits}\n")
        file.write(f"Number of other characters: {others}\n")


#Example usage:
input_filename = 'time'  # Replace with your input file path
output_filename = 'time1'  # Replace with your desired output file path

analyze_and_write(input_filename, output_filename)
print(f"Analysis written to {output_filename}")
