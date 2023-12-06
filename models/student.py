# models/student.py

from db.databases import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(10), unique=True, nullable=False)
    student_name = db.Column(db.String(50), unique=False, nullable=False)
    student_age = db.Column(db.Integer, nullable=False)
    student_email = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=True)
    score = db.Column(db.Float, nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)
    progress = db.Column(db.Integer, nullable=True, server_default="0")
