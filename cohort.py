from students import Student                                                  # Import Student class


class Cohort:                                                                 # Create Cohort/Course class
    def __init__(self, name):
        self.course_name = name
        self.students = []                                                    # Create student attribute, to store students on each course
        self.student_names_to_be_added = []

    def get_student_data(self, file_name):                                    # get_student_data method retrieves student names from a file ...
        try:                                                                  # ... and stores the names in student_names_to_be_added
            with open(file_name) as file:
                file_line_list = file.readlines()

                for line in file_line_list:
                    self.student_names_to_be_added.append(line.rstrip("\n"))

                file.close()

        except FileNotFoundError as error_message:
            print(error_message)
            raise

        finally:
            return self.student_names_to_be_added

    def add_student(self, student):                                          # add_student method adds students to a course
        self.students.append(student)

    def remove_student(self, student):                                       # remove_student method removes students from a course
        self.students.remove(student)

    def add_student_names_to_students(self):                                 # add_student_names_to_students method adds students ...
        i = len(self.students)                                               # ... from student_names_to_be_added to student attribute
        for student in self.student_names_to_be_added:
            name = student.split(" ")
            other_names = ""
            for names in name[1:]:
                other_names = other_names + " " + names
            last_names = other_names.lstrip(" ")
            new_student = Student(name[0], last_names)
            self.add_student(new_student)
            self.students[i].add_course(self)
            i += 1
        self.student_names_to_be_added = []

    def run_register(self):                                                  # run_register method checks attendance for each student
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

        percent_attendance = int((100 * (total_num_of_students - num_of_absent_students)) / total_num_of_students)
        print("\nToday we have " + str(percent_attendance)
              + "% attendance, with " + str(num_of_absent_students) + " absent.")
