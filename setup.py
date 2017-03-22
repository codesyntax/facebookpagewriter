from setuptools import setup, find_packages
import sys, os

version = '0.8'

setup(
    name='facebookpagewriter',
    version=version,
    description='Automate Facebook page posting',
    long_description="",
    author='Aitzol Naberan',
    author_email='anaberan@codesyntax.com',
    url='http://github.com/codesyntax/facebookpagewriter',
    package_dir={'facebookpagewriter': 'facebookpagewriter'},
    packages=find_packages(exclude=['ez_setup','examples','tests']),
    include_package_data=True,
    requires=['django(>=1.10)'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)
