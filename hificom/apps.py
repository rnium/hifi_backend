from django.apps import AppConfig


class HificomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hificom'

    def ready(self):
        import hificom.signals
