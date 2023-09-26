import unittest
from lms_application import LMSApplication

class TestLMSApplication(unittest.TestCase):

    def setUp(self):
        self.app = LMSApplication()

    def test_process_command(self):
        output = self.app.process_command("ADD-COURSE-OFFERING", ["Python101", "Sachin", "01012024", 10, 20])
        self.assertTrue(output.startswith("OFFERING-"))

        _, status = self.app.process_command("REGISTER", ["sachin@email.com", output])
        self.assertEqual(status, "ACCEPTED")

        _, status = self.app.process_command("CANCEL", [_])
        self.assertEqual(status, "CANCEL_ACCEPTED")
