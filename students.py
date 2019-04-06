class Student:
    def __init__(self, first_name, last_name):
        self.student_first_name = first_name
        self.student_last_name = last_name
        self.course = ""

    def student_name(self):
        return self.student_first_name + " " + self.student_last_name

    def add_course(self,course):
        self.course = course