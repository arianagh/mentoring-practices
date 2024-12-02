text = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

lines = text.strip().split("\n")

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

print("Left List:", left_list)
print("Right List:", right_list)


def question_1():
    distances = []
    for i in range(len(left_list)):
        m1 = min(left_list)
        m2 = min(right_list)
        distances.append(abs(m1 - m2))
        left_list.remove(m1)
        right_list.remove(m2)

    return sum(distances)


print(question_1())
