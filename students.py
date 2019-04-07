class Student:                                                           # Create Student class
    def __init__(self, first_name, last_name):                           # Constructor function that takes the first and last name of each student
        self.student_first_name = first_name
        self.student_last_name = last_name
        self.course = ""

    def student_name(self):                                              # student_name method that returns the students full name
        return self.student_first_name + " " + self.student_last_name

    def add_course(self,course):                                         # add_course method adds a course to the student
        self.course = course