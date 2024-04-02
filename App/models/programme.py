from App.database import db

class Programme(db.Model):
  __tablename__ = 'programme'

  p_ID = db.Column(db.Integer, primary_key = True)
  p_name = db.Column(db.String(100), nullable = False)
  # creates reverse relationship from Programme back to Course to access courses within a programme
  # coursesAssigned = db.relationship('course', backref=db.backref('course', lazy='joined'))

  def __init__(self, p_ID, name):
    self.p_ID = p_ID
    self.p_name = p_name
    
  def to_json(self):
    return {
      "programmeID": self.p_ID,
      "programmeTitle": self.p_name
    }  
