from App.models import assessment
from App.database import db

def list_assessment_types():
    return assessment.query.all() 