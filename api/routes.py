from flask import jsonify, request, Flask
from main import app
from services.admin_service import AdminServices
from services.instructor_services import InstructorService
from services.student_service import StudentService

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello there!"

@app.route('/instructors/register', methods=['POST'])
def add_new_instructor():
    try:
        instructor_data = request.get_json()

        # Create a new instructor
        new_instructor = InstructorService.register_instructor(
            instructor_id=instructor_data["instructor_id"],
            instructor_name=instructor_data["instructor_name"],
            course_id=instructor_data["course_id"],
        )

        return {"message": "Instructor registered successfully"}, 201

    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {"error": "Internal Server Error"}, 500
    
@app.route('/instructors/delete/<instructor_id>', methods=['DELETE'])
def delete_instructor(instructor_id):
    deleted_instructor_info, status_code = InstructorService.delete_instructor(instructor_id)
    return jsonify(deleted_instructor_info), status_code

@app.route('/instructors/courses/<instructor_id>', methods=['GET'])
def get_instructors_courses(instructor_id):
    instructor_course_info, status_code = InstructorService.get_instructors_and_courses(instructor_id)

    return jsonify(instructor_course_info), status_code


@app.route('/instructors/students/<course_id>', methods=['GET'])
def get_students_in_course(course_id):
    course_student_info, status_code = InstructorService.get_students_for_course(course_id)

    return jsonify(course_student_info), status_code


@app.route('/instructors/progress/<course_id>/<student_id>', methods=['GET'])
def get_student_progress_in_course(course_id, student_id):
    progress_data, status_code = InstructorService.get_student_progress(course_id, student_id)

    return jsonify(progress_data), status_code


@app.route('/admin/students', methods=['POST'])
def create_student():
    try:
        student_data = request.get_json()

        # Create a new student
        new_student = AdminServices.add_student(
            student_id=student_data["student_id"],
            student_name=student_data["student_name"],
            student_age=student_data["student_age"],
            student_email=student_data["student_email"],
        )

        return {"message": "Student registered successfully"}, 201

    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {"error": "Internal Server Error"}, 500


@app.route('/admin/students/<studentId>', methods=['PUT'])
def modify_student(studentId):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    updated_student_info, status_code = AdminServices.update_student(studentId, updated_data)
    return jsonify(updated_student_info), status_code


@app.route('/admin/courses', methods=['POST'])
def add_new_course():
    course_data = request.get_json()

    if not course_data or "course_id" not in course_data or "course_name" not in course_data:
        return jsonify({"error": "Invalid request data"}), 400

    course_info, status_code = AdminServices.add_course(
        course_id=course_data["course_id"],
        course_name=course_data["course_name"],
    )
    return jsonify(course_info), status_code


@app.route('/admin/courses/<course_id>', methods=['PUT'])
def modify_course(course_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    updated_course_info, status_code = AdminServices.update_course(course_id, updated_data)
    return jsonify(updated_course_info), status_code


@app.route('/students/register', methods=['POST'])
def add_new_student():
    try:
        student_data = request.get_json()

        # Create a new student
        new_student = StudentService.register_student(
            student_id=student_data["student_id"],
            student_name=student_data["student_name"],
            student_age=student_data["student_age"],
            student_email=student_data["student_email"],
        )

        return {"message": "Student registered successfully"}, 201

    except Exception as e:
        # Handle exceptions as needed
        print(f"Error: {e}")
        return {"error": "Internal Server Error"}, 500


@app.route('/students/info/<student_id>', methods=['GET'])
def get_student_information(student_id):
    student_info, status_code = StudentService.get_student_info(student_id)
    return jsonify(student_info), status_code


@app.route('/students/update/<student_id>', methods=['PUT'])
def modify_student_information(student_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    updated_student_info, status_code = StudentService.update_student_info(student_id, updated_data)
    return jsonify(updated_student_info), status_code

@app.route('/students/delete/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    deleted_student_info, status_code = StudentService.delete_student(student_id)
    return jsonify(deleted_student_info), status_code


@app.route('/students/courses/<student_id>', methods=['GET'])
def get_student_enrolled_courses(student_id):
    courses_data, status_code = StudentService.get_student_courses(student_id)
    return jsonify(courses_data), status_code


@app.route('/students/enroll/<student_id>/<course_id>', methods=['GET'])
def enroll_student(course_id, student_id):
    enrollment_data, status_code = StudentService.enroll_student_in_course(student_id, course_id)
    return jsonify(enrollment_data), status_code


@app.route('/students/progress/<student_id>/<course_id>', methods=['GET'])
def get_student_progress(course_id,student_id):
    progress_data, status_code = StudentService.get_student_progress_in_course(student_id, course_id)
    return jsonify(progress_data), status_code


# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404
