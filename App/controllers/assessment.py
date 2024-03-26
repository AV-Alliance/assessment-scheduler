from App.models import Assessment
from App.database import db

def list_assessment_types():
    return Assessment.query.all() 
