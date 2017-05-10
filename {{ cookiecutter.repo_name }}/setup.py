from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.python_module_name }}",
    version="1.0.0",
    packages=find_packages(exclude=['data', 'figures', 'output', 'notebooks', 'tests'])
)
