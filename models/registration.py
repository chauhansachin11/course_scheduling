class Registration:
    def __init__(self, employee, course):
        self.employee = employee
        self.course = course

    @property
    def id(self):
        return f"REG-COURSE-{self.employee.name}-{self.course.name}"
