from setuptools import setup

setup(
    name="pyMicrodata",
    description="pyMicrodata Libray",
    version="3.0",
    author="Ivan Herman",
    author_email="ivan@w3.org",
    maintainer="Ivan Herman",
    maintainer_email="ivan@w3.org",
    packages=["pyMicrodata"],
    requires=["rdflib"],
    entry_points={
        "rdf.plugins.parser": [
            "mdata = pyMicrodata.rdflibparsers:MicrodataParser",
            "microdata = pyMicrodata.rdflibparsers:MicrodataParser",
        ]
    },
)
