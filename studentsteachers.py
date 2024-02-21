from students import student

from teachers import teacher

teachers = []
students = []

def add_student(name, surname, lesson, score):
    new_student = student(name, surname, lesson, score)
    students.append(new_student)

def add_teacher(name, surname, age, lesson):
    new_teacher = teacher(name, surname, age, lesson)
    teachers.append(new_teacher)

def result_students():
    for std in students:
        print(std.show_info())

def result_teachers():
    for tch in teachers:
        print(tch.show_info())

add_student("Beril","Yılmaz","Matematik",65)
add_teacher("Alev", "İkinci", 30, "Matematik")
add_student("Ayşe", "Yücel","Felsefe",55)


result_students()
result_teachers()