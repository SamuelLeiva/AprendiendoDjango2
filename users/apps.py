from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #recomendado por los docs de django para evitar problemas de importacion
        import users.signals
