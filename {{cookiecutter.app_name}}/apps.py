"""{{ cookiecutter.app_name|capitalize }} apps module."""

# Django
from django.apps import AppConfig


class {{ cookiecutter.app_name|capitalize }}Config(AppConfig):
    """
    {{ cookiecutter.app_name|capitalize }}Config.

    {{ cookiecutter.app_name|capitalize }} application settings.
    """

    name = '{{ cookiecutter.project_slugname }}.{{ cookiecutter.app_name }}'
    app_label = '{{ cookiecutter.app_name }}'
