# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup


def get_version():
    """Get the current version of the hotness package"""
    with open("qadventure/__init__.py", "r") as fd:
        regex = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
        version = re.search(regex, fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("No version set in qadventure/__init__.py")
    return version


def get_requirements(requirements_file="requirements.txt"):
    """Get the contents of a file listing the requirements.

    :arg requirements_file: path to a requirements file
    :type requirements_file: string
    :returns: the list of requirements, or an empty list if
              `requirements_file` could not be opened or read
    :return type: list
    """

    ignored_packages = []

    lines = [
        line.rstrip().split("#")[0] for line in open(requirements_file).readlines()
    ]

    packages = []
    for line in lines:
        if line.startswith("#"):
            continue
        if any(line.startswith(package) for package in ignored_packages):
            continue
        packages.append(line)

    return packages


setup(
    name="QAdventure",
    version=get_version(),
    description="Text adventure engine written in Python and PyQt",
    license="LGPLv3",
    author="Michal Konecny",
    author_email="mkonecny@redhat.com",
    url="https://github.com/Zlopez/QAdventure",
    install_requires=get_requirements(),
    tests_require=get_requirements("dev-requirements.txt"),
    packages=find_packages(exclude=("qadventure.tests", "qadventure.tests.*")),
    test_suite="qadventure.tests",
    python_requires=">=3.8",
)
