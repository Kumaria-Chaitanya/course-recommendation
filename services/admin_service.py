# services/admin_service.py

from models.student import Student
from models.courses import Course
from db.databases import db


class AdminServices:
    def add_student(self, student_data):
        try:
            # Create a new student
            new_student = Student(
                student_id=student_data["student_id"],
                student_name=student_data["student_name"],
                course_id=student_data["course_id"],
                status=student_data.get("status"),
                score=student_data.get("score")
            )

            # Add the student to the database
            db.session.add(new_student)
            db.session.commit()

            return {"studentId": new_student.student_id, "message": "Student added successfully"}, 201

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def update_student(self,student_id, updated_data):
        try:
            # Find the student by student_id
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                # Update student information
                student.student_name = updated_data.get("student_name", student.student_name)
                student.course_id = updated_data.get("course_id", student.course_id)
                student.status = updated_data.get("status", student.status)
                student.score = updated_data.get("score", student.score)

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

    def add_course(self,course_data):
        try:
            # Create a new course
            new_course = Course(
                course_id=course_data["course_id"],
                course_name=course_data["course_name"]
            )

            # Add the course to the database
            db.session.add(new_course)
            db.session.commit()

            return {"courseId": new_course.course_id, "message": "Course added successfully"}, 201

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def update_course(self,course_id, updated_data):
        try:
            # Find the course by course_id
            course = Course.query.filter_by(course_id=course_id).first()

            if course:
                # Update course information
                course.course_name = updated_data.get("course_name", course.course_name)

                # Commit the changes to the database
                db.session.commit()

                return {"courseId": course.course_id, "message": "Course information updated successfully"}, 200
            else:
                return {"error": "Course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500
