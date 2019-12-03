import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maachujdo", # Replace with your own username
    version="1.4.1",
    author="Ventsislav Varbanovski @nu11secur1ty",
    author_email="penetrateoffensive@gmail.com",
    description="HTTP Login sniff module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nu11secur1ty/maachujdo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
