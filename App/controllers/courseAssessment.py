from App.models import Course, CourseAssessment
from App.database import db

def list_assessment_types():
    return CourseAssessment.query.all() 

def add_Assessment(courseCode, a_ID, startTime, endTime, startDate, endDate):
    # Check if new assessment is allowed
    course = db.session.query(Course).get(courseCode)
    asmAllowed = course.aNum # num of assessments allowed for course

    # Num of assessment already set for course
    asmSet = db.session.query(CourseAssessment).filter(CourseAssessment.courseCode == courseCode).count()

    if asmSet >= asmAllowed: 
        return course
    else:
         #Add new assessment
        newCourse = CourseAssessment.addCourseAsm(courseCode, a_ID, startTime, endTime, startDate, endDate)
        return newCourse
    return None  

def update_Assessment(courseCode, a_ID, startTime, endTime, startDate, endDate):
    return none    