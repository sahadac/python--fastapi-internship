class InvalidMarkError(Exception):
    pass
def calculate_grade(name, *marks):
    if len(marks) == 0:
        return name, 0, "No Marks"

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError(f"Invalid mark {mark} for {name}")
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    return name, average, grade
def generate_report(students):
    print("-" * 40)
    print(f"{'Name':<10} {'Average':<10} {'Grade':<10}")
    print("-" * 40)

    for student in students:
        try:
            name = student[0]
            marks = student[1:]

            result = calculate_grade(name, *marks)

            print(f"{result[0]:<10} {result[1]:<10.2f} {result[2]:<10}")

        except InvalidMarkError as e:
            print(f"{name:<10} ERROR      {e}")

    print("-" * 40)
students = [
    ("Sahad", 90, 95, 85),  
    ("Rahees", 150, 80, 70),
    ("Refai",),      
    ("Saad", 60, 40, 110),  
    ("Ali", 45, 50, 55)     
]
generate_report(students)