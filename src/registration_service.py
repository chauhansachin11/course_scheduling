from models.employee import Employee
from models.registration import Registration

class RegistrationService:
    def __init__(self, course_service):
        self.course_service = course_service

    def register(self, email, course_id=None):
        if not course_id:
            return "INPUT_DATA_ERROR"
        course = self.course_service.courses.get(course_id)
        if not course:
            return "INPUT_DATA_ERROR"

        if course.is_full():
            return "COURSE_FULL_ERROR"
        
        employee = Employee(email)
        registration = Registration(employee, course)
        course.add_registration(registration)

        return registration.id, "ACCEPTED"

    def allot_course(self, course_id):
        if not course_id:
            return ["INPUT_DATA_ERROR"]
        course = self.course_service.courses.get(course_id)
        if not course:
            return ["INPUT_DATA_ERROR"]
        
        if course.is_below_minimum():
            res = [(reg.id, reg.employee.email, course_id, course.name, course.instructor, course.date, "COURSE_CANCELED") for reg in course.registered]
            res.sort(key = lambda x: x[1])
            return res
        
        res = [(reg.id, reg.employee.email, course_id, course.name, course.instructor, course.date, "CONFIRMED") for reg in course.registered]
        res.sort(key = lambda x: x[1])
        return res

    def cancel(self, reg_id):
        for course in self.course_service.courses.values():
            for reg in course.registered:
                if reg.id == reg_id:
                    course.registered.remove(reg)
                    return reg.id, "CANCEL_ACCEPTED"
        return "INPUT_DATA_ERROR"
