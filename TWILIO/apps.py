from django.apps import AppConfig


class TwilioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TWILIO'

    def ready(self):
        import TWILIO.signals
