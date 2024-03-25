from flask import Blueprint, request, jsonify, render_template
from App.controllers import courseAssessment

from App.controllers.courseAssessment import (
    add_Assessment
)

asg_views = Blueprint('asg_views', __name__, template_folder='../templates')

#Gets assessments page (lists all assessments created for the courses assigned to staff)
@asg_views.route('/assessments', methods=['GET'])
def get_assessments_page():
    return render_template('assessments.html') 

# Gets Add Assessment Page
@asg_views.route('/new_asg', methods=['GET'])
def new_asg_page():
    return render_template('addAssessment.html')

# Retrieves course, asg info and stores it in database ie. add new assessment to course
@asg_views.route('/addNewAsg', methods=['POST'])
def add_asg_action():
    if request.method == 'POST':
        course = request.form.get('myCourses')
        asgType = request.form.get('AssessmentType')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endTime')
         
        courseAsg = add_Assessment(course, asgType, startTime, endTime, startDate, endDate)

        # Redirect to view assignment listings!  
        # return redirect(url_for('asg_views.assessments')) 
        return jsonify({"message":f" New assessment for {courseCode} successfully added."}), 200  #for postman

# Gets Update Assessment page
@asg_views.route('/modifyAsg', methods=['GET'])
def get_update_asg():
    return render_template('modifyAssessment.html')  

# Selects new assignment duration and time period 
@admin_views.route('/updateAsg', methods=['POST'])
def update_assessment():
    if request.method == 'POST':
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
    
    # modifyAsg(courseCode, a_ID, startTime, endTime, startDate, endDate)
    # add_Course(courseCode, title, description, level, semester, numAssessments)

    # Redirect to view assignment listings!  
    # return redirect(url_for('asg_views.assessments')) 
    return jsonify({"message":f" Assessment for {courseCode} successfully updated."}), 200 # for postman         

# Selects course and removes it from database
@asg_views.route("/deleteAsg", methods=['POST'])
def delete_asg_action(courseCode):
    if request.method == 'POST':
        course = get_course(courseCode) # Gets selected course
        # delete_Course(course)

        # Redirect to view assignment listings!  
        # return redirect(url_for('asg_views.assessments'))   
    return jsonify({"message":f" Assessment for {courseCode} successfully deleted."}), 200 # for postman
