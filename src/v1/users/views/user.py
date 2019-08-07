import json

from flask import Response, request
from flask.views import MethodView

from src.v1.users.facades.user_api import UserAPIFacade


class UserView(MethodView):
    """
    User MethodView class to define REST functions.
    Here is defined facade to UserAPI to get its data from this API.
    """

    user_api = UserAPIFacade()

    def post(self) -> Response:
        """
        User create view function.
        :return: Response with user's data
        """
        new_user, status = self.user_api.create({})
        return Response(json.dumps(new_user), status)

    def get(self, user_id: int) -> Response:
        """
        Function to get user's list or single
        instance of user object based on user_id argument.

        If argument is None, then user list will be retrieved.
        List could be parameterized by page parameter in url. Default is 1.

        :param user_id: user id
        :return: Response with user's data
        """
        if user_id:
            user_instance, status = self.user_api.retrieve(user_id)
            return Response(json.dumps(user_instance), status)

        page = request.args.get('page', 1)

        user_list, status = self.user_api.list(page)
        return Response(json.dumps(user_list), status)

    def delete(self, user_id) -> Response:
        """
        Function to delete user instance by its id.
        :param user_id:
        :return: Response
        """
        data, status = self.user_api.delete(user_id)
        return Response(json.dumps(data), status)

    def put(self, user_id) -> Response:
        """
        Function to update user instance based on its id.
        :param user_id:
        :return:
        """
        updated_user, status = self.user_api.update(user_id)
        return Response(json.dumps(updated_user), status)
