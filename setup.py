from setuptools import setup, find_packages
#import os
#import sys
# current dir
#current_dir = os.path.dirname(__file__)

# Get the absolute path to the main directory (one level up)
#main_dir = os.path.abspath(os.path.join(current_dir, ".."))

DESCRIPTION = 'This is the python package for a kernel-based consensual aggregation by S. Has (2023), and A. Fischer and M. Mougeot (2019)'
with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()

version = "1.1.4"
setup(name='gradientcobra',
      version=version,
      description='Python implementation for Gradient COBRA by S. Has (2023), and MixCOBRA by A. Fischer and M. Mougeot (2019).',
      author='Sothea Has',
      author_email="sothea.has@lpsm.paris",
      url='https://github.com/hassothea/gradientcobra/',
      packages=["gradientcobra"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Operating System :: Microsoft :: Windows',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering'
      ],
      install_requires=[
          'numpy>=1.20.1',
          'pandas>=2.1.0',
          'scipy>=1.10.1',
          'scikit-learn>=1.2',
          'matplotlib',
          'seaborn',
          'plotly>=5.10.0',
          'tqdm'
      ],
      test_suite='tests',
      keywords=[
          'Consensual aggregation',
          'Kernel',
          'Regression',
          'Statistical Aggregation'
      ],
      long_description=LONG_DESCRIPTION)
