from django.contrib import admin
from django.apps import apps
from volt.configs import VOLT_AUTOGENERATE_MENUS, VOLT_MODEL_SEARCH_FIELDS

# all other models
if VOLT_AUTOGENERATE_MENUS:
    class ListAdminMixin(object):
        def __init__(self, model, admin_site):
            self.list_display = [field.name for field in model._meta.fields]
            self.list_per_page = 15
            try:
                self.search_fields = VOLT_MODEL_SEARCH_FIELDS[f'{model._meta.app_label}.{model._meta.model_name}']
            except KeyError:
                pass
            super(ListAdminMixin, self).__init__(model, admin_site)

    models = apps.get_models()
    for model in models:
        admin_class = type(
            'AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model, admin_class)
        except admin.sites.AlreadyRegistered:
            pass
