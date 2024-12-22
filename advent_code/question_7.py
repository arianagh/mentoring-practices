from itertools import product


def parse_input(file_path):
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            target, numbers = line.split(":")
            target = int(target.strip())
            nums = list(map(int, numbers.strip().split()))
            equations.append((target, nums))
    return equations


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


def find_valid_equations(equations):
    total_calibration_result = 0

    for test_value, numbers in equations:
        num_operators = len(numbers) - 1
        valid = False
        for operators in product('+*', repeat=num_operators):
            if evaluate_expression(numbers, operators) == test_value:
                valid = True
                break

        if valid:
            total_calibration_result += test_value

    return total_calibration_result


input_file = "question_7.txt"
equations = parse_input(input_file)
total_result = find_valid_equations(equations)
print(total_result)
