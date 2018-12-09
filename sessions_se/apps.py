from django.apps import AppConfig


class SessionsSeConfig(AppConfig):
    name = 'sessions_se'

    def ready(self):
        from sessions_se import signals
