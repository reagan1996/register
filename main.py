from cohort import Cohort


# course = Cohort("Data1")
# course.get_student_data("students.txt")
# course.add_raw_student_data()
# print("Hello, time for the register?")
# total_num_of_students = len(course.students)
# num_of_absent_students = 0
# for student in course.students:
#     no_valid_answer = True
#     while no_valid_answer:
#         present = input("\nIs " + student.student_name() + " here?(y/n) ")
#         if present.lower() == "y":
#             no_valid_answer = False
#         elif present.lower() == "n":
#             num_of_absent_students += 1
#             no_valid_answer = False
#         else:
#             print("\nInvalid option entered. Please try again")
#
# print("\nToday we have " + str(int((100*(total_num_of_students - num_of_absent_students))/ total_num_of_students)) + "% attendence, with " +
#       str(num_of_absent_students) + " absent.")

course = Cohort("Data1")
course.get_student_data("students.txt")
course.add_raw_student_data()

def register():
    print("Hello, time for the register?")
    total_num_of_students = len(course.students)
    num_of_absent_students = 0
    for student in course.students:
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

    print("\nToday we have " + str(
        int((100 * (total_num_of_students - num_of_absent_students)) / total_num_of_students)) + "% attendence, with " +
          str(num_of_absent_students) + " absent.")


register()





