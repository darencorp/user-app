"""
Global util module for API.
Here must be placed function necessary for business logic.
"""
from typing import Tuple, Union

import requests
from requests import RequestException

from .config import USER_API_URL


def fetch_api_data(method: str, url: str, **kwargs) -> Tuple[Union[str, dict], int]:
    """
    Function for fetching and validating users data from external API.
    If service is unavailable - make an graceful error response.
    Otherwise - return its data.

    :param method: request method
    :param url: request url
    :param kwargs: additional options such as data for POST.
    :return: status code and error description if error or user data otherwise.
    """
    try:
        response = requests.request(method, f'{USER_API_URL}{url}', **kwargs)
    except RequestException:
        return {'error': 'External API is unavailable!'}, 503

    if not response:
        return {'error': 'External API is unavailable!'}, 503

    if not response.ok:
        return {'error': response.reason}, response.status_code

    response_data = response.json() if response.text else ''
    return response_data, response.status_code
