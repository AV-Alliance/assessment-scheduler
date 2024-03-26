from App.database import db

class CourseAssessment(db.Model):
    __tablename__ = 'courseAssessment'

    ca_ID = db.Column(db.String(9), primary_key=True)
    courseCode = db.Column(db.String(8), db.ForeignKey('course.courseCode'), nullable = False)
    a_ID = db.Column(db.Integer, db.ForeignKey('assessment.a_ID'), nullable = False)
    startDate = db.Column(db.Date, nullable = False)
    endDate = db.Column(db.Date, nullable = False)
    startTime = db.Column(db.Time, nullable = False)
    endTime = db.Column(db.Time, nullable = False)
    
    #duration should be equal to difference between startTime and endTime of assessment in minutes and hours
    # duration = db.Column(db.Numeric(4, 2), nullable = False)
    # details = db.Column(db.String(250), nullable = True)
    # weight = db.Column(db.Integer, nullable = False)

    def __init__(self, courseCode, a_ID, startTime, endTime, startDate, endDate):
        self.ca_ID = "A" + str(CourseAssessment.query.count() + 1) #auto increment count
        self.courseCode = courseCode
        self.a_ID = a_ID
        self.startTime = startTime
        self.endTime = endTime
        self.startDate = startDate
        self.endDate = endDate

    def to_json(self):
        return {
            "courseAssessmentNum" : self.ca_ID,
            "courseCode" : self.courseCode,
            "a_ID" : self.a_ID,
            "startTime" : self.startTime,
            "endTime" : self.endTime,
            "startDate" : self.startDate,
            "endDate" : self.endDate
    }

    #Add new assessment to course
    def addCourseAsm(self, courseCode, a_ID, startTime, endTime, startDate, endDate):
        newAsm = CourseAssessment(courseCode, a_ID, startTime, endTime, startDate, endDate)
        db.session.add(newAsm)  #add to db
        db.session.commit()
        return newCourse
    