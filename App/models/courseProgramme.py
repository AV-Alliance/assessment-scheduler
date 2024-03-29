from App.database import db

class CourseProgramme(db.Model):
  __tablename__ = 'courseProgramme'

  courseCode = db.Column(db.String(8), db.ForeignKey('course.courseCode'), primary_key=True, nullable = False)
  p_ID = db.Column(db.Integer, db.ForeignKey('programme.p_ID'), primary_key=True, nullable = False)  