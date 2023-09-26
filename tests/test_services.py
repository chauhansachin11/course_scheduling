import unittest
from src.course_service import CourseService
from src.registration_service import RegistrationService
from models.course import Course,CourseData

class TestServices(unittest.TestCase):

    def setUp(self):
        self.course_service = CourseService()
        self.registration_service = RegistrationService(self.course_service)

    def test_course_service_add(self):
        data = CourseData("Python101", "Sachin", "01012024", 10, 20)
        course_id = self.course_service.add_course(data)
        self.assertIn(course_id, self.course_service.courses)

    def test_registration_service_register(self):
        data = CourseData("Python101", "Sachin", "01012024", 10, 20)
        course_id = self.course_service.add_course(data)
        reg_id, status = self.registration_service.register("sachin@email.com", course_id)
        self.assertEqual(status, "ACCEPTED")
        self.assertTrue(self.course_service.courses[course_id].registered)
