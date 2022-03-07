import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django4-channels-presence",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description='Tracking socket presence in "rooms" using django-channels. Migrated to Django 4.',
    long_description=README,
    url="https://github.com/klima7/django4-channels-presence",
    author="Charlie DeTar, forked by Łukasz Klimkiewicz",
    author_email="cfd@media.mit.edu, forked by ukasz.klimkiewicz@gmail.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
