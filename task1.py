#!/usr/bin/python
print ("Numbers of student")

def get_students(num_students: int) -> list:
# Students with their grades
    students = []
    for s in range(0, num_students):
        name = input("student's name: ")
        grade = float(input("student's grade: "))
        students.append([name, grade])
    return students

def get_lowest_grade(students: list) -> float:
# The lowest grade
    lowest_grade_student = min(students, key = lambda x: x[1])
    return lowest_grade_student[1]

def get_lowest_grade_students(students: list) -> list:
# Students with the lowest grade
    return [s for s in students if s[1] == get_lowest_grade(students)]

def exclude_lowest_grade_students(students: list) -> list:
# Students with the lowest grade excluded from a list of students
    return [s for s in students if s[1] != get_lowest_grade(students)]

def get_student_names_sorted_alpha(students: list) -> list:
# List of student's sorted alphabetically
    names = [s[0] for s in students]
    return sorted(names)

def main():
    num_students = int(input())
    students = get_students(num_students)
    lowest_excluded = exclude_lowest_grade_students(students)
    second_lowest = get_lowest_grade_students(lowest_excluded)
    for name in get_student_names_sorted_alpha(second_lowest):
        print("Student with the second lowest grade: ",name)

if __name__ == '__main__':
    main()
