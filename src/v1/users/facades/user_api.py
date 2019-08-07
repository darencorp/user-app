from typing import Tuple, Union

from src.v1.utils import fetch_api_data
from src.v1.config import USERS_PER_PAGE


class UserAPIFacade:
    """
    Facade for users external API.
    """

    def list(self, page: int) -> Tuple[Union[str, dict], int]:
        """
        Function to get list of users based on page parameter.
        :param page: page number
        :return: response data or error, status code
        """
        response, status = fetch_api_data('GET', f'/users?page={page}&per_page={USERS_PER_PAGE}')

        response = response['error'] if response.get('error') else response['data']
        return response, status

    def retrieve(self, user_id: int) -> Tuple[Union[str, dict], int]:
        """
        Function to get single user instance based on user_id.
        :param user_id: user id
        :return: response data or error, status code
        """
        response, status = fetch_api_data('GET', f'/users/{user_id}')

        response = response['error'] if response.get('error') else response['data']
        return response, status

    def create(self, data: dict) -> Tuple[Union[str, dict], int]:
        """
        Function to create user instance on external API.
        Actually external API is not allowed to create user instances.
        :param data: user's data
        :return: response data or error, status code
        """
        headers = {'Content-Type': 'application/json'}
        response, status = fetch_api_data('POST', '/users', data=data, headers=headers)

        response = response if response.get('error') else response
        return response, status

    def update(self, user_id: int) -> Tuple[Union[str, dict], int]:
        """
        Function to update user's instance on external API.
        Actually external API is not allowed to update user instances.
        :param user_id: user id
        :return: response data or error, status code
        """
        headers = {'Content-Type': 'application/json'}
        response, status = fetch_api_data('PUT', f'/users/{user_id}', headers=headers)

        response = response if response.get('error') else response
        return response, status

    def delete(self, user_id: int) -> Tuple[Union[str, None], int]:
        """
        Function to delete user's instance from external API.
        Actually external API is not allowed to delete users instances.
        :param user_id: user id
        :return: response data or error, status code
        """
        response, status = fetch_api_data('DELETE', f'/users/{user_id}')

        response = response if response and response.get('error') else response
        return response, status
