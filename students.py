class Student:
    def __init__(self, name):
        self.student_name = name
        self.course = ""

    def add_course(self,course):
        self.course = course