# services/student_service.py

from models.student import Student
from models.courses import Course
from db.databases import db


class StudentService:
    def get_student_info(self,student_id):
        try:
            # Fetch information of the specified student
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                student_info = {
                    "studentId": student.student_id,
                    "studentName": student.student_name,
                    "age": student.age,  # Assuming 'age' is a field in the Student model
                    "email": student.email  # Assuming 'email' is a field in the Student model
                }

                return student_info, 200
            else:
                return {"error": "Student not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def update_student_info(self,student_id, updated_data):
        try:
            # Find the student by student_id
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                # Update student information
                student.student_name = updated_data.get("student_name", student.student_name)
                student.age = updated_data.get("age", student.age)
                student.email = updated_data.get("email", student.email)

                # Commit the changes to the database
                db.session.commit()

                return {"studentId": student.student_id, "message": "Student information updated successfully"}, 200
            else:
                return {"error": "Student not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def get_student_courses(self,student_id):
        try:
            # Fetch courses in which the specified student is enrolled
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                courses = Course.query.filter_by(id=student.course_id).all()
                courses_data = [{"courseId": course.course_id, "courseName": course.course_name} for course in courses]

                return courses_data, 200
            else:
                return {"error": "Student not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def enroll_student_in_course(self,student_id, course_id):
        try:
            # Check if the student and course exist
            student = Student.query.filter_by(student_id=student_id).first()
            course = Course.query.filter_by(course_id=course_id).first()

            if student and course:
                # Check if the student is already enrolled in the course
                existing_enrollment = Student.query.filter_by(student_id=student_id, course_id=course.id).first()

                if existing_enrollment:
                    return {"error": "Student is already enrolled in the course"}, 400

                # Enroll the student in the course
                new_enrollment = Student(student_id=student_id, course_id=course.id, status="Enrolled", score=0)
                db.session.add(new_enrollment)
                db.session.commit()

                return {"message": f"Enrolled successfully in course {course_id}"}, 201
            else:
                return {"error": "Student or course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500


    def get_student_progress_in_course(self,student_id, course_id):
        try:
            # Fetch the progress of the specified student in the specified course
            student = Student.query.filter_by(student_id=student_id).first()
            course = Course.query.filter_by(course_id=course_id).first()

            if student and course:
                # Check if the student is enrolled in the specified course
                enrollment = Student.query.filter_by(student_id=student_id, course_id=course.id).first()

                if enrollment:
                    progress_data = {
                        "courseId": course.course_id,
                        "studentId": student.student_id,
                        "progress": enrollment.progress
                    }

                    return progress_data, 200
                else:
                    return {"error": "Student is not enrolled in the specified course"}, 400
            else:
                return {"error": "Student or course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500
