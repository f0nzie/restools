# from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="restools",
    version="0.0.10",
    author="Konstantin Sermyagin, Alfonso Reyes",
    author_email="kvs@readas.net, alfonso.reyes@oilgainsanalytics.com",
    description="An Eclipse reservoir simulation binary files reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/f0nzie/restools",
    packages=setuptools.find_packages(),
    install_requires=[
      'numpy', 'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
