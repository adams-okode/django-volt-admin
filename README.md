#Django Volt Admin


Django Volt is a django admin customization for https://github.com/themesberg/volt-bootstrap-5-dashboard


Quick start
-----------

1. Add "volt" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'volt',
    ]


2. Include Templaates from the volt admin customization

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR /'volt/templates',
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to view (you'll need the Admin app enabled).