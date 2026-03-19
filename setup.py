from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements from a file and returns them as a list
    """
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Clean up newline characters
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Setup configuration
setup(
    name='mlproject',
    version='1.0.0',
    author='Youssef',
    author_email="bendhaouyoussef2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)