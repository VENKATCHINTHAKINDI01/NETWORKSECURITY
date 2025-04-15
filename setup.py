''' setup file is important because it is an essential part of the packing and distributing python projects ,
it is used to define the configuration of your prooject such as metadata, dependencies ,and more '''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
          with open('requirements.txt','r') as file:
              # read lines from file
              lines=file.readlines()
              ## process each line
              for line in lines:
                  requirement=line.strip()
                  ## ignore emptyb lines and ignore -e.
                  if requirement and requirement != '-e .':
                      requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst

print(get_requirements())


setup(
    name = 'NETWORK PROJECT',
    version = '0.0.1',
    author = 'venkat',
    author_email = 'venkatchinthakindi4@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
    
)