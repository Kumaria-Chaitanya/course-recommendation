import unittest
from unittest.mock import patch
from main import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_student(self):
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
        course_data = {
            "course_id": "C004",
            "course_name": "Introduction to Python",
            "instructor_id": "1"
        }

        response = self.app.post('/admin/courses', json=course_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": f"Course added successfully with id {course_data['course_id']}"})

    def test_modify_course(self):
        course_id = "C001"
        updated_data = {
            "course_name": "Updated Python Course"
        }

        response = self.app.put(f'/admin/courses/{course_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Course information updated successfully")


    def test_add_new_student(self):
        student_data = {
            "student_id": "2",
            "student_name": "Jonathan Doe",
            "student_age": 26,
            "student_email": "jonathan.doe@example.com"
        }

        response = self.app.post('/students/register', json=student_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Student registered successfully"})

    def test_get_student_information(self):
        student_id = "1"

        response = self.app.get(f'/students/info/{student_id}')
        self.assertEqual(response.status_code, 200)

    def test_modify_student_information(self):
        student_id = "1"
        updated_data = {
            "student_name": "Updated Name",
            "student_age": 30,
            "student_email": "updated.email@example.com",
            "progress": 40
        }

        response = self.app.put(f'/students/update/{student_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_get_student_enrolled_courses(self):
        student_id = "1"

        response = self.app.get(f'/students/courses/{student_id}')
        self.assertEqual(response.status_code, 200)

    def test_enroll_student(self):
        course_id = "C001"
        student_id = "1"

        response = self.app.get(f'/students/enroll/{student_id}/{course_id}')
        self.assertEqual(response.status_code, 201)

    def test_add_new_instructor(self):
        instructor_data = {
            "instructor_id": "9",
            "instructor_name": "Alex Adams",
            "course_id": "C001"
        }

        response = self.app.post('/instructors/register', json=instructor_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Instructor registered successfully"})

if __name__ == '__main__':
    unittest.main()
