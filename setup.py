from setuptools import setup, find_packages

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="python-steam-api",
    version="1.0.7",
    description="Python Client wrapper for Steam API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "steam",
        "steamapi",
        "steam community",
        "api",
    ],
    author="David Salazar",
    author_email="david.asal@hotmail.com",
    url="https://github.com/deivit24/steam-python-sdk",
    packages=find_packages(),
    install_requires=["requests", "python-decouple"],
    license="MIT",
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python",
    ],
)
