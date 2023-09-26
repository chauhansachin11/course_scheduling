class Employee:
    def __init__(self, email):
        self.email = email
        self.name = email.split('@')[0]
