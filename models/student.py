# models/student.py

from db.databases import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(10), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=True)  # Assuming status can be nullable
    score = db.Column(db.Float, nullable=True)  # Assuming score can be nullable
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
