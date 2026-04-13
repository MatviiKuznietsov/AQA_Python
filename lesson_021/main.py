from database import init_db
from seed import seed_data
from services.student_service import add_student, get_courses_by_student
from services.course_service import get_students_by_course

def main():
    init_db()

    seed_data()

    add_student("Ivan Ivanov", 20, "Programming")

    print(get_students_by_course("Math"))
    print(get_courses_by_student("Ivan Ivanov"))

if __name__ == "__main__":
    main()