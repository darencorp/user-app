"""
Module to define endpoint to app views.

Views could be added to endpoint via blueprint.register_view()
or just via blueprint.add_url_rule()
"""

from src.utils import NestableBlueprint
from .views.user import UserView

users_blueprint = NestableBlueprint('users', __name__)
users_blueprint.register_view(UserView.as_view('users'), '/', pk='user_id')
