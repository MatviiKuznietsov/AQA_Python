from pony.orm import db_session
from lesson_021.models import Student, Course
import random

@db_session
def seed_data():
    course_titles = ["Math", "Physics", "Biology", "History", "Programming"]
    courses = [Course(title=title) for title in course_titles]

    for i in range(20):
        student = Student(
            name=f"Student_{i+1}",
            age=random.randint(18, 25)
        )
        student.courses = random.sample(courses, random.randint(1, 3))