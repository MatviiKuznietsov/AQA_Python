from pony.orm import db_session
from lesson_021.models import Course

@db_session
def get_students_by_course(course_title):
    course = Course.get(title=course_title)
    if not course:
        return []

    return [s.name for s in course.students]