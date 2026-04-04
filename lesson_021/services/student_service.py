from pony.orm import db_session
from lesson_021.models import Student, Course

@db_session
def add_student(name, age, course_title):
    course = Course.get(title=course_title)
    if not course:
        raise ValueError("Course not found")

    student = Student(name=name, age=age)
    student.courses.add(course)

    return student

@db_session
def get_courses_by_student(student_name):
    student = Student.get(name=student_name)
    if not student:
        return []

    return [c.title for c in student.courses]

@db_session
def update_student(student_name, new_name=None, new_age=None):
    student = Student.get(name=student_name)
    if not student:
        return None

    if new_name:
        student.name = new_name
    if new_age:
        student.age = new_age

    return student

@db_session
def delete_student(student_name):
    student = Student.get(name=student_name)
    if student:
        student.delete()