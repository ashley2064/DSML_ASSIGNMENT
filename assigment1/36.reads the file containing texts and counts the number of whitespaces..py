def count_whitespaces(time):
    whitespace_count = 0
    with open(time, 'r') as file:
        for line in file:
            whitespace_count += line.count(' ')
    print(f"Number of whitespaces: {whitespace_count}")

#Example usage
filename = 'time'  # Replace with your file path
count_whitespaces(filename)
