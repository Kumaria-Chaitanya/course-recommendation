# models/instructor.py

from db.databases import db


class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.String(10), unique=True, nullable=False)
    instructor_name = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)
