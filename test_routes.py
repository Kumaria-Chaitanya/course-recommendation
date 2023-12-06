import unittest
from main import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_student(self):
        # Assuming a valid JSON for the test
        student_data = {
            "student_id": "1",
            "student_name": "John Doe",
            "student_age": 20,
            "student_email": "john.doe@example.com"
        }

        response = self.app.post('/admin/students', json=student_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Student registered successfully"})

    def test_modify_student(self):
        # Assuming an existing student_id for the test
        student_id = "1"
        updated_data = {
            "student_name": "Updated Name",
            "student_age": 25,
            "student_email": "updated.email@example.com"
        }

        response = self.app.put(f'/admin/students/{student_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Student information updated successfully")

    def test_add_new_course(self):
        # Assuming a valid JSON for the test
        course_data = {
            "course_id": "C001",
            "course_name": "Introduction to Python"
        }

        response = self.app.post('/admin/courses', json=course_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": f"Course added successfully with id {course_data['course_id']}"})

    def test_modify_course(self):
        # Assuming an existing course_id for the test
        course_id = "C001"
        updated_data = {
            "course_name": "Updated Python Course"
        }

        response = self.app.put(f'/admin/courses/{course_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Course information updated successfully")


    def test_add_new_student(self):
        # Assuming a valid JSON for the test
        student_data = {
            "student_id": "2",
            "student_name": "Jonathan Doe",
            "student_age": 26,
            "student_email": "jonathan.doe@example.com"
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
        self.assertEqual(response.status_code, 201)

        # Add more test cases as needed

    def test_get_student_progress(self):
        # Assuming existing course_id and student_id for the test
        course_id = "C001"
        student_id = "1"

        response = self.app.get(f'/students/progress/{student_id}/{course_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
