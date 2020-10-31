from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InterkassaConfig(AppConfig):
    name = 'sw_interkassa'
    verbose_name = _("Оплата")
    verbose_name_plural = verbose_name


default_app_config = 'sw_interkassa.InterkassaConfig'



