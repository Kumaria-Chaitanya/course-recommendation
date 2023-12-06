# services/admin_service.py

from models.student import Student
from models.courses import Course
from db.databases import db


class AdminServices:
    def add_student(student_id, student_name, student_age, student_email):
        try:
            existing_enrollment = Student.query.filter_by(student_id=student_id).first()

            if existing_enrollment:
                return {"error": "Student already exists"}, 400

            # Enroll the student in the course
            new_student = Student(student_id=student_id, student_name=student_name, student_age=student_age, student_email=student_email)
            db.session.add(new_student)
            db.session.commit()

            return {"message": f"Student registered successfully with id {student_id}"}, 201
    
        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def update_student(student_id, updated_data):
        try:
            # Find the student by student_id
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                # Update student information
                student.student_name = updated_data.get("student_name", student.student_name)
                student.age = updated_data.get("student_age", student.student_age)
                student.email = updated_data.get("student_email", student.student_email)
                student.course_id = updated_data.get("course_id", student.course_id)
                student.status = updated_data.get("status", student.status)
                student.score = updated_data.get("score", student.score)
                student.progress = updated_data.get("progress", student.progress)

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

    def add_course(course_id,course_name):
        try:
            existing_course = Course.query.filter_by(course_id=course_id).first()

            if existing_course:
                return {"error": "Course already exists"}, 400

            # Create a new course
            new_course = Course(course_id=course_id, course_name=course_name)

            # Add the course to the database
            db.session.add(new_course)
            db.session.commit()

            return {"message": f"Course added successfully with id {courseId}"}, 201

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def update_course(course_id, updated_data):
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
