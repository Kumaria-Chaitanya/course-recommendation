# services/instructor_service.py

from models.courses import Course
from models.instructor import Instructor
from models.student import Student
from db.databases import db


class InstructorService:
    def get_instructors_and_courses(self):
        try:
            # Fetch courses and associated instructors
            courses = Course.query.all()
            courses_data = []

            for course in courses:
                instructors = Instructor.query.filter_by(course_id=course.id).all()
                instructors_data = [
                    {"instructor_id": instructor.instructor_id, "instructor_name": instructor.instructor_name}
                    for instructor in instructors]

                course_data = {
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "instructors": instructors_data
                }

                courses_data.append(course_data)

            return courses_data

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return None

    def get_students_for_course(self, course_id):
        try:
            # Fetch students enrolled in the specified course
            course = Course.query.filter_by(course_id=course_id).first()

            if course:
                students = Student.query.filter_by(course_id=course.id).all()
                students_data = [{"student_id": student.student_id, "student_name": student.student_name}
                                 for student in students]

                return students_data
            else:
                return {"error": "Course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def get_student_progress(self, course_id, student_id):
        try:
            # Fetch progress of the specified student in the specified course
            course = Course.query.filter_by(course_id=course_id).first()

            if course:
                student = Student.query.filter_by(student_id=student_id, course_id=course.id).first()

                if student:
                    return {"courseId": course.course_id, "studentId": student.student_id, "progress": student.progress}
                else:
                    return {"error": "Student not found"}, 404
            else:
                return {"error": "Course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500
