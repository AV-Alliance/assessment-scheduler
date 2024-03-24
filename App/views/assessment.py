from flask import Blueprint, request, jsonify, render_template
from App.controllers import Course

asg_views = Blueprint('asg_views', __name__, template_folder='../templates')

# Gets Add Assessment Page
@asg_views.route('/new_asg', methods=['GET'])
def new_asg_page():
    return render_template('addAssessment.html')

# Retrieves course, asg info and stores it in database ie. add new assessment to course
@admin_views.route('/addNewAsg', methods=['POST'])
def add_asg_action():
    if request.method == 'POST':
        courseCode = request.form.get('course_code')
        title = request.form.get('title')
        description = request.form.get('description')
        level = request.form.get('level')
        semester = request.form.get('semester')
        numAssessments = request.form.get('numAssessments')
         
        course = add_Course(courseCode,title,description,level,semester,numAssessments)

        # Redirect to view course listings!  
        # return redirect(url_for('admin_views.get_courses')) 
        return jsonify({"message":f" {courseCode} successfully added to course listings."}), 200  #for postman
