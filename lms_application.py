from src.course_service import CourseService
from src.registration_service import RegistrationService
from models.course import CourseData

class LMSApplication:
    def __init__(self):
        self.course_service = CourseService()
        self.registration_service = RegistrationService(self.course_service)

    def process_command(self, command, params):
        if command == "ADD-COURSE-OFFERING":
            data = CourseData(*params)
            return self.course_service.add_course(data)
        elif command == "REGISTER":
            return self.registration_service.register(*params)
        elif command == "ALLOT":
            return self.registration_service.allot_course(params[0])
        elif command == "CANCEL":
            return self.registration_service.cancel(params[0])
        else:
            return "INPUT_DATA_ERROR"
        
    def execute(self, input_file):
        with open(input_file, 'r') as f:
            for line in f:
                command, *params = line.strip().split()
                output = self.process_command(command, params)
                self.print_output(output)

    def print_output(self, output):
        if type(output) == tuple:
            print(" ".join(map(str, output)))
        elif type(output) == list:
            for item in output:
                print(" ".join(map(str, item)))
        else:
            print(output)
