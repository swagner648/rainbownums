import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rainbownums",
    version="1.4",
    author="Simon Wagner",
    author_email="swagner648@gmail.com",
    description="Python package to solve anti-Schur equations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
)
