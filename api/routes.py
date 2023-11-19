from flask import jsonify, request, Flask
from main import app
from services.admin_service import AdminServices
from services.instructor_services import InstructorService
from services.student_service import StudentService

app = Flask(__name__)


@app.route('/instructors/courses', methods=['GET'])
def get_instructors_courses():
    courses_data = InstructorService.get_instructors_and_courses()
    if courses_data is not None:
        return jsonify(courses_data), 200
    else:
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/instructors/students/<courseId>', methods=['GET'])
def get_students_in_course(course_id):
    students_data = InstructorService.get_students_for_course(course_id)

    if isinstance(students_data, list):
        return jsonify(students_data), 200
    else:
        return jsonify(students_data), students_data.get("status", 500)


@app.route('/instructors/progress/{courseId}/{studentId}', methods=['GET'])
def get_student_progress_in_course(course_id, student_id):
    progress_data = get_student_progress(course_id, student_id)

    if isinstance(progress_data, dict):
        return jsonify(progress_data), 200
    else:
        return jsonify(progress_data), progress_data.get("status", 500)


@app.route('/admin/students', methods=['POST'])
def create_student():
    data = request.get_json()

    if not data or "student_id" not in data or "student_name" not in data or "course_id" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    result = AdminServices.add_student(data)
    return jsonify(result), result.get("status", 500)


@app.route('/admin/students/{studentId}', methods=['PUT'])
def modify_student(studentId):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    result = AdminServices.update_student(studentId, updated_data)
    return jsonify(result), result.get("status", 500)


@app.route('/admin/courses', methods=['POST'])
def add_new_course():
    data = request.get_json()

    if not data or "course_id" not in data or "course_name" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    result = AdminServices.add_course(data)
    return jsonify(result), result.get("status", 500)


@app.route('/admin/courses/<course_id>')
def modify_course(course_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    result = AdminServices.update_student(course_id, updated_data)
    return jsonify(result), result.get("status", 500)


@app.route('/students/register', methods=r['POST'])
def add_new_student():
    pass


@app.route('/students/info/<student_id>', methods=['GET'])
def get_student_information(student_id):
    student_info, status_code = StudentService.get_student_info(student_id)
    return jsonify(student_info), status_code


@app.route('/students/update/<student_id>', methods=['PUT'])
def modify_student_information(student_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    result = StudentService.update_student_info(student_id, updated_data)
    return jsonify(result), result.get("status", 500)


@app.route('/students/courses/<student_id>', methods=['GET'])
def get_student_enrolled_courses(student_id):
    courses_data, status_code = StudentService.get_student_courses(student_id)
    return jsonify(courses_data), status_code


@app.route('/students/enroll/<student_id>/<course_id>', methods=['POST'])
def enroll_student(course_id, student_id):
    result = StudentService.enroll_student_in_course(student_id, course_id)
    return jsonify(result), result.get("status", 500)


@app.route('/students/progress/student_id/<course_id>', methods=['GET'])
def get_student_progress(course_id,student_id):
    progress_data, status_code = StudentService.get_student_progress_in_course(student_id, course_id)
    return jsonify(progress_data), status_code


# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404
