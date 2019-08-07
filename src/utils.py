"""
Utils module to separate all of system required functions in one place.
"""

from flask import Blueprint
from flask.views import MethodView


class NestableBlueprint(Blueprint):
    """
    Flask has a problem with recursive blueprints.
    So we can just make own blueprint class and make
    here function for adding nested blueprints.
    """

    def register_blueprint(self, blueprint: 'NestableBlueprint', **kwargs) -> None:
        """
        Method to register nested blueprint.
        We can get URL for endpoint from from extra arguments or from blueprint.
        Than we add them to base URL and delete them from extra arguments
        in purpose to not override then on later steps.

        Then blueprint is registered to base app.

        :param blueprint: blueprint to register
        :param kwargs: external arguments
        """
        def deferred(state):
            url_prefix = (state.url_prefix or '') + (kwargs.get('url_prefix', blueprint.url_prefix) or '')
            if 'url_prefix' in kwargs:
                del kwargs['url_prefix']

            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **kwargs)

        self.record(deferred)

    def register_view(self, view: MethodView, url: str, pk: str = 'id', pk_type: str = 'int') -> None:
        """
        Method to register standard function set for MethodView.
        There are standard REST method for view.
         GET for list instances
         GET for single instance
         POST to create instance
         PUT to update instance
         DELETE to delete instnce

        :param view: MethodView instance
        :param url: endpoint URL
        :param pk: primary key for single instance
        :param pk_type: type of primary key
        :return:
        """
        self.add_url_rule(url, defaults={pk: None}, view_func=view, methods=['GET', ])
        self.add_url_rule(url, view_func=view, methods=['POST', ])
        self.add_url_rule('%s<%s:%s>/' % (url, pk_type, pk), view_func=view, methods=['GET', 'PUT', 'DELETE'])
