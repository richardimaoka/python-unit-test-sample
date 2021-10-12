from setuptools import setup, find_packages

setup(
    name="ppkg",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # root package is under the 'src' directory
    install_requires=['click==7.1.2', 'tinydb==3.15.1', 'six'],
)
