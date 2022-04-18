import unittest

from test.student import Student


class TestStudent(unittest.TestCase):
    def test_if_given_data_are_correct_none(self):
        deni=Student("deni",None)
        self.assertEqual("deni", deni.name)
        self.assertEqual({}, deni.courses)

    def test_if_given_data_are_correct_dict_given(self):
        deni=Student("deni",{1:2})
        self.assertEqual("deni", deni.name)
        self.assertEqual({1:2}, deni.courses)
    """    def enroll(self, course_name: str, notes, add_course_notes: str = ""):
        if course_name in self.courses.keys():
            [self.courses[course_name].append(x) for x in notes]
            return "Course already added. Notes have been updated."""
    def test_enroll_name_in_courses_add_notes_succes(self):
        deni = Student("deni", {"Python": []})
        result=deni.enroll("Python",[1,2,3],"d")
        self.assertEqual({"Python": [1,2,3]}, deni.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_and_course_notes__add_succes_in_empty_courses_Y(self):
        deni = Student("deni", {})
        result=deni.enroll("Python",[1,2,3],"Y")
        self.assertEqual({"Python": [1,2,3]}, deni.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_and_course_notes__add_succes_in_empty_courses_emty_string(self):
        deni = Student("deni", {})
        result = deni.enroll("Python", [1, 2, 3], "")
        self.assertEqual({"Python": [1, 2, 3]}, deni.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_add_empty_cource_to_dict(self):
        deni = Student("deni", {})
        result=deni.enroll("Python",[1,2,3],"dd")
        self.assertEqual({"Python": []}, deni.courses)
        self.assertEqual("Course has been added.", result)

    """    def add_notes(self, course_name, notes):
        if course_name in self.courses.keys():
            self.courses[course_name].append(notes)
            return "Notes have been updated"
        raise Exception("Cannot add notes. Course not found.")"""
    def test_add_notes__have_such_course__rerturn_string(self):
        deni = Student("deni", {"Python": []})
        result = deni.add_notes("Python", 5)
        self.assertEqual({"Python": [5]}, deni.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes__NO_such_course__raise_exception(self):
        deni = Student("deni", {})
        with self.assertRaises(Exception) as context:
            deni.add_notes("Python", 5)
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))
    """    def leave_course(self, course_name):
        if course_name in self.courses.keys():
            self.courses.pop(course_name)
            return "Course has been removed"
        raise Exception("Cannot remove course. Course not found.")"""

    def test_leave__if_course_in_courses__remove_it(self):
        deni = Student("deni", {"Python": []})
        result = deni.leave_course("Python")
        self.assertEqual({}, deni.courses)
        self.assertEqual("Course has been removed", result)
    def test_leave__NO_such_course__raise_exception(self):
        deni = Student("deni", {})
        with self.assertRaises(Exception) as context:
            deni.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))






if __name__=="__main__":
    unittest.main()
