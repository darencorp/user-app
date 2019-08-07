"""
Module to define things necessary for testing.
"""

import json


class UserAPIResponseMock:
    """
    Mock response object from external API.
    """

    def __init__(self, **kwargs):
        """
        Constructor could pass any parameter necessary for testing.
        :param kwargs: any parameters
        """
        self.__dict__.update(kwargs)

    def json(self) -> dict:
        """
        Mock of json() function in response object.
        :return: dict
        """
        return json.loads(self.text)
