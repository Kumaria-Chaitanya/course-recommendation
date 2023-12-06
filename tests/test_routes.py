import unittest
from flask import Flask, json
from main import app
from services.student_service import StudentService

class TestStudentRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_add_new_student(self):
        # Assuming a valid JSON for the test
        student_data = {
            "student_id": "1",
            "student_name": "John Doe",
            "student_age": 25,
            "student_email": "john.doe@example.com"
        }

        response = self.app.post('/students/register', json=student_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Student registered successfully"})

        # Add more test cases as needed

    def test_get_student_information(self):
        # Assuming an existing student_id for the test
        student_id = "1"

        response = self.app.get(f'/students/info/{student_id}')
        self.assertEqual(response.status_code, 200)

        # Add more test cases as needed

    def test_modify_student_information(self):
        # Assuming an existing student_id and valid JSON for the test
        student_id = "1"
        updated_data = {
            "student_name": "Updated Name",
            "student_age": 30,
            "student_email": "updated.email@example.com"
        }

        response = self.app.put(f'/students/update/{student_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Add more test cases as needed

    def test_get_student_enrolled_courses(self):
        # Assuming an existing student_id for the test
        student_id = "1"

        response = self.app.get(f'/students/courses/{student_id}')
        self.assertEqual(response.status_code, 200)

        # Add more test cases as needed

    def test_enroll_student(self):
        # Assuming existing course_id and student_id for the test
        course_id = "C001"
        student_id = "1"

        response = self.app.get(f'/students/enroll/{student_id}/{course_id}')
        self.assertEqual(response.status_code, 200)

        # Add more test cases as needed

    def test_get_student_progress(self):
        # Assuming existing course_id and student_id for the test
        course_id = "C001"
        student_id = "1"

        response = self.app.get(f'/students/progress/{student_id}/{course_id}')
        self.assertEqual(response.status_code, 200)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
