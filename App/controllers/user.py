from flask import jsonify
from flask_jwt_extended import create_access_token, set_access_cookies
from App.models import User, Admin, Staff
    

def validate_Staff(email, password):
    staff = Staff.query.filter_by(email=email).first()
    for s in staff:
        if s and s.check_password(password):
            return s
    return None

def validate_Admin(email, password):
    admin = Admin.query.filter_by(email=email).first()
    if admin and admin.check_password(password):
        return admin
    return None

def get_user(email, password):
    user = validate_Staff(email, password)
    if user != None:
        return user
    user = validate_Admin(email, password)
    if user !=None:
        return user
    return None

def login_user(email, password):
  user = User.query.filter_by(email=email).first()
  if user and user.check_password(password):
    token = create_access_token(identity=email)
    response = jsonify(access_token=token)
    set_access_cookies(response, token)
    return response
  return jsonify(message="Invalid username or password"), 401
