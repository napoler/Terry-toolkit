import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Terry_toolkit',
    version='0.0.1.6.2.5',
    description='Terry toolkit',
    author='Terry Chan',
    author_email='napoler2008@gmail.com',
    url='https://terry-toolkit.terrychan.org/zh/master/',
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
