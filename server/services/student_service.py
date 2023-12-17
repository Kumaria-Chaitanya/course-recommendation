# services/student_service.py

from models.student import Student
from models.courses import Course
from db.databases import db
from sqlalchemy import and_
from models.course_student import course_student

class StudentService:
    def register_student(student_id, student_name, student_age, student_email):
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

    def get_student_info(student_id):
        try:
            # Fetch information of the specified student
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                student_info = {
                    "studentId": student.student_id,
                    "studentName": student.student_name,
                    "age": student.student_age,
                    "email": student.student_email
                }

                return student_info, 200
            else:
                return {"error": "Student not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def update_student_info(student_id, updated_data):
        try:
            # Find the student by student_id
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                # Update student information
                student.student_name = updated_data.get("student_name", student.student_name)
                student.age = updated_data.get("student_age", student.student_age)
                student.email = updated_data.get("student_email", student.student_email)

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
        
    def delete_student(student_id):
        try:
            # Fetch the student to be deleted
            student = Student.query.filter_by(student_id=student_id).first()

            if student:
                # Delete the student from the database
                db.session.delete(student)
                db.session.commit()

                return {"message": "Student deleted successfully"}, 200
            else:
                return {"error": "Student not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def get_student_courses(student_id):
        try:
            # Fetch courses in which the specified student is enrolled
            student = Student.query.filter_by(student_id=student_id).first()
            courses = student.courses

            if not courses:
                return {"error": "Student is not  enrolled in any course"}, 400

            courses_data = [{"courseId": course.course_id, "courseName": course.course_name} for course in courses]
            return courses_data, 200
        
        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def enroll_student_in_course(student_id, course_id):
        try:
            # Check if the student and course exist
            student = Student.query.filter_by(student_id=student_id).first()
            course = Course.query.filter_by(course_id=course_id).first()

            print(student)
            print(course)

            if student and course:
                # Check if the student is already enrolled in the course
                print("Inside if")
                #existing_enrollment = student.courses.filter_by(course_id=course_id).first()

                #if existing_enrollment:
                 #   return {"error": "Student is already enrolled in the course"}, 400

                print("after exisiting enrollement")
                # Enroll the student in the course
                student.courses.append(course)

                # Update the progress in the association table
                #enrollment = course_student.update().values(progress=0).where(
                 #   and_(
                  #      course_student.c.student_id == student.student_id,
                   #     course_student.c.course_id == course.course_id
                    #)
                #)
                print("before execution")
                #db.session.execute(enrollment)

                # Commit the changes to the database
                db.session.commit()

                return {"message": f"Enrolled successfully in course {course_id}"}, 201
            else:
                return {"error": "Student or course not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500



    def get_student_progress_in_course(student_id, course_id):
        try:
            # Fetch the progress of the specified student in the specified course
            student = Student.query.filter_by(student_id=student_id).first()
            course = Course.query.filter_by(course_id=course_id).first()

            if student and course:
                # Check if the student is enrolled in the specified course
                enrollment = Student.query.filter_by(student_id=student_id, course_id=course_id).first()

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
