from cohort import Cohort
import unittest

class Cohorttests(unittest.TestCase):



    def test_get_student_data(self):
        self.test_cohort = Cohort("Test")
        self.assertEqual(["Test Student1", "Test Student2", "Test Student 3", "Test"], self.test_cohort.get_student_data("test_student_data.txt"))

    def test_add_raw_student_data(self):
        self.test_cohort = Cohort("Test")
        self.test_cohort.get_student_data("test_student_data.txt")
        self.test_cohort.add_raw_student_data()
        self.assertEqual("Test Student1",self.test_cohort.students[0].student_name())

    def test_first_and_last_name(self):
        self.test_cohort = Cohort("Test")
        self.test_cohort.get_student_data("test_student_data.txt")
        self.test_cohort.add_raw_student_data()
        self.assertEqual("Test",self.test_cohort.students[0].student_first_name)

    def test_middle_name(self):
        self.test_cohort = Cohort("Test")
        self.test_cohort.get_student_data("test_student_data.txt")
        self.test_cohort.add_raw_student_data()
        self.assertEqual("Student 3", self.test_cohort.students[2].student_last_name)

    def test_no_last_name(self):
        self.test_cohort = Cohort("Test")
        self.test_cohort.get_student_data("test_student_data.txt")
        self.test_cohort.add_raw_student_data()
        self.assertEqual("", self.test_cohort.students[3].student_last_name)

