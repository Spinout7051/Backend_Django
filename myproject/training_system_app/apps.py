from django.apps import AppConfig


class TrainingSystemAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'training_system_app'

    def ready(self):
        from . import signals
