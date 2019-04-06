from students import Student


class Cohort:
    def __init__(self, name):
        self.course_name = name
        self.students = []
        self.students_raw = []

    def get_student_data(self, file_name):
        try:
            with open(file_name) as file:
                file_line_list = file.readlines()

                for line in file_line_list:
                    self.students_raw.append(line.rstrip("\n"))

                file.close()

        except FileNotFoundError as error_message:
            print(file_name + " not found")
            print(error_message)
            raise

        finally:
            return self.students_raw

    def add_students(self, student):
        self.students.append(student)

    def add_raw_student_data(self):
        i = len(self.students)
        for student in self.students_raw:
            new_student = Student(student)
            self.add_students(new_student)
            self.students[i].add_course(self)
            i += 1
