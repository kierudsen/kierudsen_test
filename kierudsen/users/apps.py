from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "kierudsen.website"
    verbose_name = _("Website")

    def ready(self):
        try:
            import kierudsen.users.signals  # noqa F401
        except ImportError:
            pass

