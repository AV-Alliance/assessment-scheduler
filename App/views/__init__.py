from .staff import staff_views
from .index import index_views
from .admin import admin_views
from .course import course_views
from .user import user_views
from .auth import auth_views

views = [staff_views, index_views, admin_views, course_views, user_views, auth_views]
# blueprints must be added to this list^^
