from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='myTesla',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/zmsp/python-my-tesla',
    license='Apache License 2.0',
    author='Zobair Shahadat',
    author_email='cheezyspam21@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Python client to interact with your tesla.',
    classifiers=[
        "Operating System :: OS Independent",
    ],
)
