from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="1.0.0",
    packages=find_packages(include=['{{ cookiecutter.project_slug }}',])
)
