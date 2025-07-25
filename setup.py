from setuptools import find_packages,setup
from typing import List

def get_pacakges() -> List[str]:

    requirements_lst:List[str] = []
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")
    return requirements_lst

setup(
    name = "networksecurity",
    version = "0.0.1",
    author = "Mithilesh Goud",
    author_email = "mithileshburra@gmail.com"
    packages = find_packages(),
    install_requires = get_requirements()

)