from setuptools import setup, find_packages

project_name = 'End to End Machine learning project'
my_version = '0.0.1'


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list:

    """
    This function returns a list of requirements from the given file path 
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



setup(
    name = project_name,
    version = my_version,
    author = 'Akande soji',
    author_email = 'akandesoji4christ@gmail.com',
    description = 'A project to build an end-to-end machine learning project',
    url = 'https://github.com/harcuracy/machine_learning_project',
    packages = find_packages(),
    install_requires = [get_requirements('requirements.txt')],
)