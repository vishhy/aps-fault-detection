## setup.py file will turn our code into a python package. Thus, we can install that code on any device through pip

from setuptools import find_packages, setup
from typing import List


REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."   # Editable Installation

def get_requirements()->List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()

    # Replacing \n at the end of every package name
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    # Removing -e ., required for installing the code as a package, will trigger the setup.py file
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
    

setup(
    name="sensor",
    version="0.0.1",
    author="vishwas",
    author_email="sharma.vishwas7788@gmail.com",
    packages=find_packages(),    # Any folder containing __int__.py is considered as Python Package/Library
    install_requires=get_requirements()
)