# {{ cookiecutter.project_name}}

## Getting started (building your virtual environment)
In the file `environment.yml` you'll find the most common dependencies.
If there are dependencies you think you'll need which are not on the list, don't worry, it is very easy to add them later on.
To create a new environment from the file, run the following command from your DSVM terminal (which you got from ssh or putty):

    conda env create -f environment.yml

You can now create notebooks in the `notebooks` directory from this environment, which is named after your project.

## Working with secrets
Storing secrets in git is **bad**. Real bad. To counter this, the [dotenv](https://github.com/theskumar/python-dotenv) package is present in your environment.
With this package, you can store your secrets without worrying they will end up in git, and still use them in your projects.
To use the `dotenv` package, add a new `.env` file to your project (this file will not be picked up by git), and add your secrets like so:

    SECRET=value

In `{{ cookiecutter.repo_name }}/settings.py`, you will find the following lines:

    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    
These lines make sure you can now access the secrets (in your `settings.py` file) as if they were standard environmental variables:

    SECRET = os.environ.get("SECRET")

## Versioning your code
It is recommended to use semver (semantic versioning) for your code. In this definition, your version numbers look like `<breaking>.<feature>.<bugfix>`, or `<major>.<minor>.<patch>`. Your features are likely the result of a sprint, while your bugfixes happen more frequently. However, it is very important to make sure you increase the major (breaking) version number whenever you introduce changes that make older code incompatible. 

Because it can be hard to keep track of where the version is stored and what version you are on, the `bumpversion` package is installed. With this tool, bumping the version number is as easy as:

    bumpversion <major / minor / patch>
    
This will increase the version number in your setup.py, create a commit stating the version has changed, and tag the commit with the new version, so you never forget to do any of these steps.
