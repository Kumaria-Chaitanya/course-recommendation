# associations.py

from db.databases import db

course_student = db.Table(
    'course_student',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.student_id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.course_id')),
    db.Column('progress', db.Integer, nullable=True, server_default="0")
)
