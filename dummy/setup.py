from setuptools import setup
from distutils.core import setup
from setuptools import find_packages

setup(
    name='KalProjects',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # If any package contains *.exe, *.xml, *.xsd, or *.yaml files, include them:
        '': ['*.exe', '*.xml', '*.xsd', '*.yaml'],
    },
)
