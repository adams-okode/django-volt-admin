from setuptools import setup, find_packages

extras_require = {
    'lint': [
        'pep8',
    ],
    'dev': [
        'bumpversion>=0.5.3,<1',
        'wheel',
        'twine',
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +
    extras_require['lint']
)

setup(
    name='django-volt-admin',
    version='1.0.2',
    description='Django admin implementation of volt admin dashboard',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url='https://github.com/adams-okode/django-volt-admin',
    author='Adams Okode',
    author_email='adamsokode@gmail.com',
    license='MIT',
    packages=find_packages(
        exclude=['tests', 'tests.*', 'licenses', 'requirements']),
    install_requires=[
        'Django>=2.2',
    ],
    extras_require=extras_require,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
