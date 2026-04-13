from pony.orm import Required, Set, PrimaryKey
from database import db

class Student(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)
    courses = Set("Course")

class Course(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    students = Set(Student)