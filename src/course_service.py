from models.course import Course, CourseData

class CourseService:
    def __init__(self):
        self.courses = {}

    def add_course(self, course_data: CourseData):
        course = Course(course_data)
        self.courses[course.id] = course
        return course.id
