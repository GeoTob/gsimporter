#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = "gsimporter",
    version = "0.1",
    description = "GeoServer Importer Client",
    keywords = "GeoServer Importer",
    license = "MIT",
    url = "https://github.com/opengeo/gsimporter",
    author = "Ian Schneider",
    author_email = "ischneider@opengeo.org",
    install_requires = [
        'httplib2',
    ],
    package_dir = {'':'src'},
    packages = find_packages('src'),
) 

