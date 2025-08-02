def sum_and_average(input, output):
    numbers = []

    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit() or (line.startswith('-') and line[1:].isdigit()):
                numbers.append(int(line))

    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0

    with open(output, 'w') as file:
        file.write(f"Sum: {total}\n")
        file.write(f"Average: {avg}\n")

    print(f"Sum: {total}")
    print(f"Average: {avg}")

#   Call the function with your files
sum_and_average("input", "output")



