from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

name = "maya_template_project"
version = "0.1.0"
author = "Martin L'Anton"
author_email = "lantonmartin@gmail.com"
description = "Template python package for Maya projects"

url = "https://github.com/martinlanton/tox_template_project"

python_requires = ">=3.6, <4"

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    url=url,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=python_requires,
)
