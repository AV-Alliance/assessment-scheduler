from flask import Blueprint, flash, redirect, request, jsonify, render_template
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from flask_login import logout_user
from App.controllers.auth import login
from App.models.user import User
from App.models.staff import Staff
from App.database import db

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
    
@auth_views.route('/login', methods=['POST'])
def login_action():
    email = request.form.get('email')
    password = request.form.get('password')
    response = login_user(email, password)
    if not response:
        flash('Bad email or password given'), 401 
    return response

def login_user(email, password):
    user = db.session.query(Staff).filter(Staff.email == email).first()
    if user and user.check_password(password):
        token = create_access_token(identity=email)
        response = jsonify(access_token = token)
        set_access_cookies(response, token)
        return response
    return jsonify(message="Invalid username or password"), 401

@auth_views.route('/logout', methods=['GET'])
@jwt_required()
def logout():
  logout_user()
  return render_template('login.html')  

# @auth_views.route('/identify')
# @jwt_required()
# def identify_view():
#   email = get_jwt_identity()
#   user = User.query.filter_by(email=email).first()
#   if user:
#     return jsonify(user.to_json())
#   return jsonify(message='Invalid user'), 403