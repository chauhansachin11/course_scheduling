import unittest
from models.course import Course,CourseData
from models.employee import Employee
from models.registration import Registration

class TestModels(unittest.TestCase):

    def test_course_creation(self):
        data = CourseData("Python101", "Sachin", "01012024", 10, 20)
        course = Course(data)
        self.assertEqual(course.name, "Python101")
        self.assertEqual(course.instructor, "Sachin")

    def test_employee_creation(self):
        employee = Employee("sachin@email.com")
        self.assertEqual(employee.name, "sachin")
        self.assertEqual(employee.email, "sachin@email.com")

    def test_registration_creation(self):
        data = CourseData("Python101", "Sachin", "01012024", 10, 20)
        course = Course(data)
        employee = Employee("sachin@email.com")
        registration = Registration(employee, course)
        self.assertEqual(registration.id, "REG-COURSE-sachin-Python101")
