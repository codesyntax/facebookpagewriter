from setuptools import setup, find_packages
import sys, os

version = '0.5'

setup(name='facebookpagewriter',
      version=version,
      description="Automate Facebook page posting",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='facebook page',
      author='Aitzol Naberan',
      author_email='anaberan@codesyntax.com',
      url='http://www.codesyntax.com/products/facebookpagewriter',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'facebook-sdk',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
