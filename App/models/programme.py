from App.database import db

class Programme(db.Model):

  __tablename__ = 'programme'

  p_ID = db.Column(db.Integer, primary_key = True)
  p_name = db.Column(db.String(100), nullable = False)
  # programmeCourses = db.relationship('coursePrograme', backref = 'programme' )