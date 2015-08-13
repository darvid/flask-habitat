"""
    Flask-Habitat
    =============

    Selectively load Flask configuration values from environment variables at
    runtime.
"""
from setuptools import setup


setup(
    name="Flask-Habitat",
    version="0.1",
    url="https://github.com/darvid/flask-habitat/",
    license="BSD",
    author="David Gidwani",
    author_email="david.gidwani@gmail.com",
    description=("Selectively load Flask configuration values from "
                 "environment variables at runtime."),
    long_description=__doc__,
    py_modules=["flask_habitat"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "Flask"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
