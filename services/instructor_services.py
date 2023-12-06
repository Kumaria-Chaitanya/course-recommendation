# services/instructor_service.py

from models.courses import Course
from models.instructor import Instructor
from models.student import Student
from db.databases import db


class InstructorService:
    def register_instructor(instructor_id, instructor_name, course_id):
        try:
            existing_enrollment = Instructor.query.filter_by(instructor_id=instructor_id).first()

            if existing_enrollment:
                return {"error": "Instructor already exists"}, 400

            # Enroll the instructor in the course
            new_instructor = Instructor(instructor_id=instructor_id, instructor_name=instructor_name, course_id=course_id)
            db.session.add(new_instructor)
            db.session.commit()

            return {"message": f"Instructor registered successfully with id {instructor_id}"}, 201
    
        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500
        
    def delete_instructor(instructor_id):
        try:
            # Fetch the instructor to be deleted
            instructor = Instructor.query.filter_by(instructor_id=instructor_id).first()

            if instructor:
                # Delete the instructor from the database
                db.session.delete(instructor)
                db.session.commit()

                return {"message": "Instructor deleted successfully"}, 200
            else:
                return {"error": "Instructor not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            db.session.rollback()
            return {"error": "Internal Server Error"}, 500

    def get_instructors_and_courses(instructor_id):
        try:
            # Fetch courses in which the specified instructor is enrolled
            instructor = Instructor.query.filter_by(instructor_id=instructor_id).first()

            if instructor:
                courses = Course.query.filter_by(course_id=instructor.course_id).all()
                if not courses:
                    return {"error": "Instructor is not  enrolled in any course"}, 400

                courses_data = [{"courseId": course.course_id, "courseName": course.course_name} for course in courses]

                return courses_data, 200
            else:
                return {"error": "Instructor not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500


    def get_students_for_course(course_id):
        try:
            # Fetch students enrolled in the specified course
            course = Course.query.filter_by(course_id=course_id).first()

            if course:
                students = Student.query.filter_by(course_id=course_id).all()
                students_data = [{"student_id": student.student_id, "student_name": student.student_name}
                                 for student in students]

                return students_data, 200
            else:
                return {"error": "Course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500

    def get_student_progress(course_id, student_id):
        try:
            # Fetch progress of the specified student in the specified course
            course = Course.query.filter_by(course_id=course_id).first()

            if course:
                student = Student.query.filter_by(student_id=student_id, course_id=course_id).first()

                if student:
                    return {"courseId": course.course_id, "studentId": student.student_id, "progress": student.progress}, 200
                else:
                    return {"error": "Student not found"}, 404
            else:
                return {"error": "Course not found"}, 404

        except Exception as e:
            # Handle exceptions as needed
            print(f"Error: {e}")
            return {"error": "Internal Server Error"}, 500
