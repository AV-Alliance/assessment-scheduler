from App.models import CourseAssessment
from App.controllers import get_course
from App.database import db

def add_Assessment(courseCode, a_ID, startTime, endTime, startDate, endDate):
    # Check if new assessment is allowed
    # Num of assessments allowed for course
    course = get_course(courseCode)
    asgAllowed = course.aNum

    # Num of assessment already in course
    aNum = db.session.query(CourseAssessment).filter(CourseAssessment.courseCode == courseCode).count()

    if aNum >= asgAllowed: 
        return course
    else:
         #Add new assessment
        newCourse = CourseAssessment.addCourseAsg(courseCode, courseTitle, description, level, semester, aNum)
        return newCourse
    return None  

def update_Assessment(courseCode, a_ID, startTime, endTime, startDate, endDate):
    return none    