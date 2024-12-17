#### complicated and inefficient solution ####

# def check_valid(rules, update):
#     for rule in rules:
#         if rule[0] in update and rule[1] in update:
#             fi = update.index(rule[0])
#             si = update.index(rule[1])
#             if fi > si:
#                 return False
#     return True
#
#
# def total_sum():
#     buf = []
#     for update in updates:
#         if check_valid(rules, update):
#             middle = len(update) // 2
#             buf.append(update[middle])
#
#     return sum(buf)
#
#
# print(total_sum())


def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split("\n\n")

    rules = [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]

    return rules, updates


def is_update_valid(rules, update):
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True


def calculate_middle_sum(rules, updates):
    return sum(update[len(update) // 2] for update in updates if is_update_valid(rules, update))


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def part_1_solution(rules, updates):
    return calculate_middle_sum(rules, updates)


# --------------------------------------------------------------------------

def swap(update, fi, si):
    update[fi], update[si] = update[si], update[fi]


def correct_order(update, rules):
    swapped = True
    while swapped:
        swapped = False
        for x, y in rules:
            if x in update and y in update:
                fi = update.index(x)
                si = update.index(y)
                if fi > si:
                    swap(update, fi, si)
                    swapped = True
    return update


def part_two_sum(rules, updates):
    incorrect_updates = [update for update in updates if not is_update_valid(rules, update)]
    corrected_middles = []

    for update in incorrect_updates:
        corrected_update = correct_order(update.copy(), rules)
        middle = len(corrected_update) // 2
        corrected_middles.append(corrected_update[middle])

    return sum(corrected_middles)


def main():
    file_path = "question_5.txt"
    input_text = read_input_file(file_path)
    rules, updates = parse_input(input_text)
    print(part_1_solution(rules, updates))
    print(part_two_sum(rules, updates))


if __name__ == "__main__":
    main()
