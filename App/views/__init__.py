from .staff import staff_views
from .index import index_views
from .admin import admin_views
from .course import course_views
from .assessment import asg_views

views = [staff_views, index_views, admin_views, course_views, asg_views]
# blueprints must be added to this list^^
