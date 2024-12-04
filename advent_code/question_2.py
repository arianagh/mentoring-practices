file_path = "question_2.txt"

rows = []

with open(file_path, "r") as file:
    for line in file:
        row = list(map(int, line.split()))
        rows.append(row)

num_rows = len(rows)


def part_1_solution(rows):
    count = 0
    for row_index in range(len(rows)):
        first = rows[row_index][0]
        second = rows[row_index][1]
        incr = True
        flag = False
        for i in range(len(rows[row_index]) - 1):
            if first > second:
                incr = False

            if not incr:
                if rows[row_index][i] < rows[row_index][i + 1]:
                    flag = False
                    break
            if incr:
                if rows[row_index][i] > rows[row_index][i + 1]:
                    flag = False
                    break

            if rows[row_index][i] == rows[row_index][i + 1]:
                flag = False
                break

            if abs(rows[row_index][i] - rows[row_index][i + 1]) > 3:
                flag = False
                break

            flag = True

        if flag:
            count += 1

    return count


print(part_1_solution(rows))


def is_safe_report(report):
    """
    Check if a report is safe based on the rules:
    1. Levels must be strictly increasing or strictly decreasing.
    2. Adjacent levels must differ by at least 1 and at most 3.
    """
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check for increasing pattern
        if diff < 1 or diff > 3:
            increasing = False

        # Check for decreasing pattern
        if -diff < 1 or -diff > 3:
            decreasing = False

        # If neither pattern is maintained, break early
        if not increasing and not decreasing:
            return False

    return increasing or decreasing


def is_safe_with_dampener(report):
    """
    Check if a report is safe, considering the Problem Dampener.
    If removing one level makes the report safe, it counts as safe.
    """
    # First, check if the report is safe without modification
    if is_safe_report(report):
        return True

    # Try removing each level and check if the modified report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True

    return False


def count_safe_reports(reports, use_dampener=False):
    """
    Count the number of safe reports. If `use_dampener` is True,
    use the dampener logic to allow one bad level to be removed.
    """
    safe_count = 0
    for report in reports:
        if use_dampener:
            if is_safe_with_dampener(report):
                safe_count += 1
        else:
            if is_safe_report(report):
                safe_count += 1
    return safe_count


# Part One: Without the Problem Dampener
# safe_count = count_safe_reports(rows, use_dampener=False)
# print("Number of safe reports without dampener:", safe_count)

# Part Two: With the Problem Dampener
safe_count_with_dampener = count_safe_reports(rows, use_dampener=True)
print("Number of safe reports with dampener:", safe_count_with_dampener)
