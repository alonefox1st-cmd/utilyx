from setuptools import setup, find_packages

setup(
    name="utilyx",
    version="1.0.0",
    description="A lightweight Python utility module for config loading, writing, and safe exits.",
    author="alonefox",
    author_email="alonefox_1st@hotmail.com",
    url="https://github.com/alonefox1st-cmd/utilyx",
    packages=find_packages(),
    python_requires=">=3.8",
    keywords=["utility", "config", "json", "ini", "tools"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)