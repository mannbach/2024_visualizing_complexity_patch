"""Script to install local packages
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="patch-workshop",
    version="0.0.2",
    author="Jan Bachmann",
    author_email="bachmann@csh.ac.at",
    description=("[P]referential [A]ttachment [T]riadic [C]losure and [H]omophily."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mannbach/2024_visualizing_complexity_patch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="patch_workshop"),
    python_requires=">=3.9",
)
