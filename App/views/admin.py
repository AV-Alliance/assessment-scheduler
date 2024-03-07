from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from App.database import db
#from flask_jwt_extended import current_user as jwt_current_user
#from flask_jwt_extended import jwt_required

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

# Gets Semester Details Page
@admin_views.route('/semester', methods=['GET'])
def get_upload_page():
    return render_template('semester.html')

# Retrieves semester details and stores it in database 
@admin_views.route('/newSemester', methods=['POST'])
def new_semester_action():
    if request.method == 'POST':
        semBegins = request.form.get('teachingBegins')
        semEnds = request.form.get('teachingEnds')
        sem = request.form.get('semester')
        
        # Store values in gloabal variables
        # Return page to upload cvs file for courses offered that semester
        return render_template('index.html')  
               