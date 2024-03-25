from flask import Blueprint, request, jsonify, render_template
from App.controllers import courseAssessment

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
        endTime = request.form.get('endTime')
         
        courseAsg = add_Assessment(courseCode, a_ID, startTime, endTime, startDate, endDate)

        # Redirect to view assignment listings!  
        # return redirect(url_for('asg_views.assessments')) 
        return jsonify({"message":f" New assessment for {courseCode} successfully added."}), 200  #for postman

# # Gets Update Assessment page
# @admin_views.route('/modifyAsg/<string:courseCode>', methods=['GET'])
# def get_update_course(courseCode):
#     # course = get_course(courseCode) # Gets selected course

#     return render_template('modifyAssessment.html')  

# # Selects new course details and updates existing course in database
# @admin_views.route('/updateCourse', methods=['POST'])
# def update_course():
#     if request.method == 'POST':
#         courseCode = request.form.get('code')
#         title = request.form.get('title')
#         description = request.form.get('description')
#         level = request.form.get('level')
#         semester = request.form.get('semester')
#         numAssessments = request.form.get('assessment')
#         programme = request.form.get('programme')
    
#     delete_Course(get_course(courseCode))
#     add_Course(courseCode, title, description, level, semester, numAssessments)

#     # Redirect to view course listings! 
#     # return redirect(url_for('admin_views.get_courses')) 
#     return jsonify({"message":f" {courseCode} successfully updated."}), 200 # for postman         
