from students import Student


class Cohort:
    def __init__(self, name):
        self.course_name = name
        self.students = []
        self.raw_student_data = []

    def get_student_data(self, file_name):
        try:
            with open(file_name) as file:
                file_line_list = file.readlines()

                for line in file_line_list:
                    self.raw_student_data.append(line.rstrip("\n"))

                file.close()

        except FileNotFoundError as error_message:
            print(error_message)
            raise

        finally:
            return self.raw_student_data

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_raw_student_data(self):
        i = len(self.students)
        for student in self.raw_student_data:
            name = student.split(" ")
            last_names = ""
            for names in name[1:]:
                last_names = last_names + " " + names
            other_names = last_names.lstrip(" ")
            new_student = Student(name[0], other_names)
            self.add_student(new_student)
            self.students[i].add_course(self)
            i += 1
        self.raw_student_data = []

    def run_register(self):
        print("Hello, time for the register?")
        total_num_of_students = len(self.students)
        num_of_absent_students = 0
        for student in self.students:
            no_valid_answer = True
            while no_valid_answer:
                present = input("\nIs " + student.student_name() + " here?(y/n) ")
                if present.lower() == "y":
                    no_valid_answer = False
                elif present.lower() == "n":
                    num_of_absent_students += 1
                    no_valid_answer = False
                else:
                    print("\nInvalid option entered. Please try again")

        percent_attendence = int((100 * (total_num_of_students - num_of_absent_students)) / total_num_of_students)
        print("\nToday we have " + str(percent_attendence)
              + "% attendence, with " + str(num_of_absent_students) + " absent.")
