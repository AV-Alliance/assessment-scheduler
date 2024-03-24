from App.database import db

class CourseAssessment(db.Model):
    __tablename__ = 'courseAssessment'

    courseCode = db.Column(db.String(8), db.ForeignKey('course.courseCode'), primary_key= True, nullable = False)
    a_ID = db.Column(db.Integer, db.ForeignKey('assessment.a_ID'), primary_key= True, nullable = False)
    startDate = db.Column(db.Date, nullable = False)
    endDate = db.Column(db.Date, nullable = False)
    startTime = db.Column(db.Time, nullable = False)
    endTime = db.Column(db.Time, nullable = False)
    
    #duration should be equal to difference between startTime and endTime of assessment in minutes and hours
    # duration = db.Column(db.Numeric(4, 2), nullable = False)
    # details = db.Column(db.String(250), nullable = True)
    # weight = db.Column(db.Integer, nullable = False)

    def __init__(self, courseCode, a_ID, startTime, endTime, startDate, endDate):
        self.courseCode = courseCode
        self.a_ID = a_ID
        self.startTime = startTime
        self.endTime = endTime
        self.startDate = startDate
        self.endDate = endDate

    def to_json(self):
        return {
            "courseCode" : self.courseCode,
            "a_ID" : self.a_ID,
            "startTime" : self.startTime,
            "endTime" : self.endTime,
            "startDate" : self.startDate,
            "endDate" : self.endDate
    }

    #Add new assessment to course
    def addCourseAsg(self, courseCode, a_ID, startTime, endTime, startDate, endDate):
        newAsg = CourseAssessment(courseCode, a_ID, startTime, endTime, startDate, endDate)
        db.session.add(newAsg)  #add to db
        db.session.commit()
        return newCourse
    