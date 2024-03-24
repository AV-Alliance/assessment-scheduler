from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from App.controllers import Staff
from App.controllers import Course
from App.database import db
#from flask_jwt_extended import current_user as jwt_current_user
#from flask_jwt_extended import jwt_required

from App.controllers.staff import (
    register_staff
)

from App.controllers.course import (
    list_Courses
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')

# Gets Signup Page
@staff_views.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

# Gets Login Page
@staff_views.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')  

# Gets Calendar Page
@staff_views.route('/calendar', methods=['GET'])
def get_calendar_page():
    return render_template('index.html')        
 
# Retrieves info and stores it in database ie. register new staff
@staff_views.route('/register', methods=['POST'])
def register_staff_action():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        staffID = request.form.get('staffID')
        status = request.form.get('status')
        email = request.form.get('email')
        pwd = request.form.get('password')
         
        # Flash message
        if (firstName == '' or lastName == '' or staffID == '' or status == '' or email == '' or pwd == ''):
            return render_template('signup.html', message = 'Please enter required fields.')
        else:
            register_staff(firstName, lastName, staffID, status, email, pwd)
            return render_template('index.html')  
            # return jsonify({"message":f" {status} registered with id {staffID}"}), 200 # for postman
    
#Gets account page
@staff_views.route('/account', methods=['GET'])
def get_account_page():
    courses=list_Courses()
    return render_template('account.html', courses=courses)        

#Gets assessments page (lists all assessments created for the courses assigned to staff)
@staff_views.route('/assessments', methods=['GET'])
def get_assessments_page():
    return render_template('assessments.html')      
