from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from App.database import db
from werkzeug.utils import secure_filename
import os
#from flask_jwt_extended import current_user as jwt_current_user
#from flask_jwt_extended import jwt_required

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

# Ensures that variables are set just once on application startup!
@admin_views.before_app_first_request
def set_variables():
    global semBegins
    global semEnds
    global semChoice

# Gets Semester Details Page
@admin_views.route('/semester', methods=['GET'])
def get_upload_page():
    return render_template('semester.html')

# Gets Course Listings Page
@admin_views.route('/coursesList', methods=['GET'])
def index():
    return render_template('courses.html')    

# Retrieves semester details and stores it in global variables 
@admin_views.route('/newSemester', methods=['POST'])
def new_semester_action():
    if request.method == 'POST':
        semBegins = request.form.get('teachingBegins')
        semEnds = request.form.get('teachingEnds')
        semChoice = request.form.get('semester')
        
        # Return course upload page to upload cvs file for courses offered that semester
        return render_template('test.html')  
               
# Uploads course details file
@admin_views.route('/uploadcourse', methods=['POST'])
def upload_course_file():
    if request.method == 'POST':
        # Check if file is present
        if 'file' not in request.files:
            return 'No file selected!'

        file = request.files['file']

        # Check if file name is present
        if file.filename == '':
            return 'No selected file!'

        # Secure filename
        filename = secure_filename(file.filename)

        # Save file to upload folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        return f'File uploaded successfully'

# Retrieves course details from file and stores it in database ie. store course info         
@admin_views.route('/parseFile', methods=['POST'])
def parse_course_file():
    if request.method == 'POST':
        return render_template('courses.html') 