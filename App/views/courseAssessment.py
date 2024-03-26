from flask import Blueprint, request, jsonify, render_template
from App.controllers import courseAssessment, assessment, Staff

from App.controllers.courseAssessment import (
    add_Assessment
)

from App.controllers.assessment import (
    list_assessment_types
)

from App.controllers.staff import(
    get_registered_courses
)

asm_views = Blueprint('asm_views', __name__, template_folder='../templates')

#Gets assessments page (lists all assessments created for the courses assigned to staff)
@asm_views.route('/assessments', methods=['GET'])
def get_assessments_page():
    registered_courses=get_registered_courses(123)
    return render_template('assessments.html', courses=registered_courses)      

# Gets Add Assessment Page
@asm_views.route('/new_asm', methods=['GET'])
def new_asg_page():
    types = list_assessment_types()
    registered=get_registered_courses(123)
    return render_template('addAssessment.html', types=types, courses=registered)

# Retrieves course, asg info and stores it in database ie. add new assessment to course
@asm_views.route('/addNewAsm', methods=['POST'])
def add_asg_action():
    if request.method == 'POST':
        course = request.form.get('myCourses')
        asgType = request.form.get('AssessmentType')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        print(course, asgType, startTime, endTime, startDate, endDate)
        courseAsg = add_Assessment(course, asgType, startTime, endTime, startDate, endDate)

        # Redirect to view assignment listings!  
        # return redirect(url_for('asm_views.assessments')) 
        return jsonify({"message":f" New assessment for {course} successfully added."}), 200  #for postman

# Gets Update Assessment page
@asm_views.route('/modifyAsg/<string:ca_ID>', methods=['GET'])
def get_update_asg():
    return render_template('modifyAssessment.html')  

# Selects new assignment duration and time period 
@asm_views.route('/updateAsg', methods=['POST'])
def update_assessment():
    if request.method == 'POST':
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
    
    # modifyAsg(courseCode, a_ID, startTime, endTime, startDate, endDate)
    # add_Course(courseCode, title, description, level, semester, numAssessments)

    # Redirect to view assignment listings!  
    # return redirect(url_for('asm_views.assessments')) 
    return jsonify({"message":f" Assessment for {courseCode} successfully updated."}), 200 # for postman         

# Selects course and removes it from database
@asm_views.route("/deleteAsg", methods=['POST'])
def delete_asg_action(courseCode):
    if request.method == 'POST':
        course = get_course(courseCode) # Gets selected course
        # delete_Course(course)

        # Redirect to view assignment listings!  
        # return redirect(url_for('asm_views.assessments'))   
    return jsonify({"message":f" Assessment for {courseCode} successfully deleted."}), 200 # for postman
