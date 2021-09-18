# Django Volt Admin
Django Volt is a django admin customization for https://github.com/themesberg/volt-bootstrap-5-dashboard

Samples
----------
![alt text](https://raw.githubusercontent.com/adams-okode/django-volt-admin/main/docs/login.png)

![alt text](https://raw.githubusercontent.com/adams-okode/django-volt-admin/main/docs/dashboard.png)
Quick start
-----------
1. Install 
    ```bash
    pip install django-volt-admin
    ```

2. Add "volt" to your INSTALLED_APPS setting like this::
    ```python
    INSTALLED_APPS = [
        'volt',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
       
    ]
    ```
    ensure that the app is declared before django admin

3. Include Templates from the volt admin customization
    ```python
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
    ```

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to view (you'll need the Admin app enabled).