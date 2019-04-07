from cohort import Cohort

course = Cohort("Data1")
course.get_student_data("students.txt")
course.add_student_names_to_students()
course.run_register()
