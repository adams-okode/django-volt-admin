from django.conf import settings

VOLT_ADMIN_SIDEBAR_ICONS = getattr(settings, 'VOLT_ADMIN_SIDEBAR_ICONS', {
    'admin': 'security',
    'auth': 'account-group',
    'contenttypes': 'solid',
    'sessions': 'solid',
    'test_data': 'book-open'
})
VOLT_AUTOGENERATE_MENUS = getattr(settings, 'VOLT_AUTOGENERATE_MENUS', False)
VOLT_MODEL_SEARCH_FIELDS = getattr(settings, 'VOLT_MODEL_SEARCH_FIELDS', {
    'admin.logentry': [],
    'auth.permission': [],
    'auth.group': [],
    'auth.user': [],
    'contenttypes.contenttype': [],
})

VOLT_ADMIN_LIST_FILTERS = getattr(settings, 'VOLT_ADMIN_LIST_FILTERS', {
    'test_data': ()
})
