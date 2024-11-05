def calculate_average(grades):
    return sum(grades) / len(grades)

def write_average_to_file(filename, average):
    with open(filename, 'w') as file:
        file.write(f"The average grade is: {average:.2f}")

# Example usage
grades = [85, 90, 78, 92, 88]
average = calculate_average(grades)
write_average_to_file('average_grade.txt', average)

print("Average grade calculated and written to average_grade.txt")
