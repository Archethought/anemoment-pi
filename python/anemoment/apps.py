from django.apps import AppConfig


class AnemomentConfig(AppConfig):
    name = 'anemoment'

    def ready(self):
        """
        Runs on application startup.
        """
        print("Hello World")
