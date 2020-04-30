# -*- coding: utf-8 -*-

import os
import sys
import addendum

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


with open('README.rst') as f:
    readme = f.read()


setup(
    name='django-addendum-wagtail',
    version=addendum.__version__,
    description='Simple template-based content swapping for use with the Wagtail CMS',
    long_description=readme,
    author='Chris Hawes',
    author_email='chrishawes@gmail.com',
    url='https://github.com/cjh9/django-addendum-wagtail',
    license='BSD License',
    packages=find_packages(exclude=['tests']),
    platforms=['OS Independent'],
    install_requires=[
        'django',
        'wagtail',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    include_package_data=True,
)
