from App.database import db

class CourseAssessment(db.Model):
    __tablename__ = 'courseAssessment'

    courseCode = db.Column(db.String(8), db.ForeignKey('course.courseCode'), primary_key= True, nullable = False)
    a_ID = db.Column(db.Integer, db.ForeignKey('assessment.a_ID'), primary_key= True, nullable = False)
    startDate = db.Column(db.Date, nullable = False)
    endDate = db.Column(db.Date, nullable = False)
    startTime = db.Column(db.Time, nullable = False)
    endTime = db.Column(db.Time, nullable = False)
    
    # More features to add for possible extension
    # duration = db.Column(db.Numeric(4, 2), nullable = False)
    # details = db.Column(db.String(250), nullable = True)
    # weight = db.Column(db.Integer, nullable = False)

    def __init__(self, courseCode, a_ID, startDate, endDate, startTime, endTime):
        self.courseCode = courseCode
        self.a_ID = a_ID
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime

    def to_json(self):
        return {
            "courseCode" : self.courseCode,
            "a_ID" : self.a_ID,
            "startDate" : self.startDate,
            "endDate" : self.endDate,
            "startTime" : self.startTime,
            "endTime" : self.endTime
        }

    #Add new assessment to course
    def addCourseAsg(self, courseCode, a_ID, startDate, endDate, startTime, endTime):
        newAsg = CourseAssessment(courseCode, a_ID, startDate, endDate, startTime, endTime)
        db.session.add(newAsg)  #add to db
        db.session.commit()
        return newCourse