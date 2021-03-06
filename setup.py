import os
from setuptools import setup
import sys

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

tests_require = ['responses>=0.5']
if sys.version_info < (3, 3):
    tests_require.append('mock>=1.3')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-moj-irat',
    version='0.3',
    packages=['moj_irat'],
    include_package_data=True,
    license='BSD License',
    description="Tools to support adding a Django-based service to "
                "Ministry of Justice's Incidence Response and Tuning",
    long_description=README,
    install_requires=['Django>=1.8', 'requests'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: MoJ Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='runtests.runtests',
    tests_require=tests_require
)
