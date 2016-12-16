
import os
import codecs
from setuptools import setup

HERE = os.path.dirname(__file__)
README = os.path.join(HERE, 'README.rst')
with codecs.open(README, 'r', encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

setup(name="pyMicrodata",
      description=LONG_DESCRIPTION,
      version="2.0",
      author="Ivan Herman",
      author_email="ivan@w3.org",
	  maintainer="Ivan Herman",
	  maintainer_email="ivan@w3.org",
      url='https://github.com/RDFLib/pymicrodata',
      packages=['pyMicrodata'],
	  install_requires = ['rdflib'])

