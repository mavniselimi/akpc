import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mavniselimi", # Replace with your own username
    version="0.0.1",
    author="pc",
    author_email="ferob9124@gmail.com",
    description="A module for close pc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mavniselimi/akpc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
