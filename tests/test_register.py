from cohort import Cohort
import unittest

class Cohorttests(unittest.TestCase):



    def test_get_student_data(self):
        self.test_cohort_1 = Cohort("Test")
        self.assertEqual(["Test Student1", "Test Student2"], self.test_cohort_1.get_student_data("test_student_data.txt"))

    def test_add_raw_student_data(self):
        self.test_cohort_2 = Cohort("Test")
        self.test_cohort_2.get_student_data("test_student_data.txt")
        self.test_cohort_2.add_raw_student_data()
        self.assertEqual("Test Student1",self.test_cohort_2.students[0].student_name)



