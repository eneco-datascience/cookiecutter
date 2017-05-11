from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.repo_name }}",
    version="1.0.0",
    packages=find_packages(include=['{{ cookiecutter.repo_name }}',])
)
