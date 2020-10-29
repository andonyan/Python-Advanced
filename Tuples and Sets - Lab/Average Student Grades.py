def get_student_grades(n):

    grades = {}

    for _ in range(n):
        record = input().split()
        name = record[0]
        grade = float(record[1])

        if name in grades:
            grades[name].append(grade)
        else:
            grades[name] = [grade]

    return grades


def print_student_grades(dictionary):

    for name, grades_list in dictionary.items():
        print(f'{name} -> {" ".join("%.2f" % x for x in grades_list)} (avg: {sum(grades_list) / len(grades_list):.2f})')


print_student_grades(get_student_grades(int(input())))
