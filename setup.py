from setuptools import setup, find_packages

setup(
    name="ppkg",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # root package is under the 'src' directory
)
