# models/course.py

from db.databases import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(10), unique=True, nullable=False)
    course_name = db.Column(db.String(255), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructor.instructor_id"))
