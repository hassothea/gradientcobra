from setuptools import setup, find_packages
#import os
#import sys
# current dir
#current_dir = os.path.dirname(__file__)

# Get the absolute path to the main directory (one level up)
#main_dir = os.path.abspath(os.path.join(current_dir, ".."))

DESCRIPTION = 'This is the python package for a kernel-based consensual aggregation by S. Has (2023)'
with open('README.txt') as f:
    LONG_DESCRIPTION = f.read()

version = "0.0.1"
setup(name='gradientcobra',
      version=version,
      description='Python implementation for Gradient COBRA: A kernel-based consensual aggregation for regression by S. Has (2023).',
      author=['Sothea Has'],
      author_email=['sothea.has@lpsm.paris'],
      url='https://github.com/hassothea/gradientcobra/',
      packages=find_packages(where = "gradientcobra"),
      install_requires=[
          'numpy',
          'pandas'
          'scipy',
          'scikit-learn',
          'matplotlib',
          'seaborn',
          'pandas'

      ],
      test_suite='tests',
      keywords=[
          'Consensual aggregation',
          'Kernel',
          'Regression',
          'Statistical Aggregation'
      ],
      long_description=LONG_DESCRIPTION)
