from setuptools import setup, find_packages


setup(
    name='txmetrics',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'robotframework',
        'robotframework-selenium2library',
        'robotframwework-screencaplibrary',
        'git+https://github.com/bluehat8/custom-robotmetrics-report.git'
    ],
)

#python setup.py sdist

#pip install txmetrics-1.0.tar.gz

