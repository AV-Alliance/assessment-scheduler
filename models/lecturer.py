from App.database import db

class Status(enum.Enum):
    PTINSTRUCT = "Part-Time Instructor"
    INSTRUCTOR = "Instructor"
    HOD = "Head of Department"
    LECTURER = "Lecturer"
    TA = "Teaching Assisstant"
    TUTOR = "Tutor"
    PTTUTOR = "Part-Time Tutor"

class Admin(User):
  __tablename__ = 'lecturer'

  fName = db.Column(db.String(120), nullable=False)
  lName = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False)
  cNum = db.Column(db.Integer, nullable=False, default=0)
  #Defines the contract position of a teaching staff member
  status = db.Column(db.Enum(Status), nullable = False)
  #creates reverse relationship from Lecturer back to Course to access courses assigned to a specific lecturer
  coursesAssigned = db.relationship('course', backref=db.backref('courses', lazy='joined'))

  def __init__(self, fName, lName, email, cNum):
    super().__init__(u_ID, password)
    self.fName = fName
    self.lName = lName
    self.email = email
    self.cNum = cNum


  def register(self, fName, lName, email):
    newLect = Lecturer(self, fName, lName, email)
    db.session.add(newLect)  #add to db
    db.session.commit()
    return newLect  

