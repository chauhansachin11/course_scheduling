from dataclasses import dataclass

@dataclass
class CourseData:
    name: str
    instructor: str
    date: str
    min_employees: int
    max_employees: int


class Course:
    def __init__(self, course_data: CourseData):
        self.name = course_data.name
        self.instructor = course_data.instructor
        self.date = course_data.date
        self.min_employees = int(course_data.min_employees)
        self.max_employees = int(course_data.max_employees)
        self.registered = []

    @property
    def id(self):
        return f"OFFERING-{self.name}-{self.instructor}"

    def is_full(self):
        return len(self.registered) >= self.max_employees

    def is_below_minimum(self):
        return len(self.registered) < self.min_employees

    def add_registration(self, registration):
        self.registered.append(registration)
