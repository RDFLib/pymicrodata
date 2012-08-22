pyMicrodata distiller/parser library. The distribution contains:

- ./pyMicrodata: the Python library. You should copy the directory
  somewhere into your PYTHONPATH. Alternatively, you can also run the

    python setup.py install

  script in the directory.

- ./scripts/CGI_microdata.py: can be used as a CGI script to invoke the library.
  It has to be adapted to the local server setup, namely in setting the right paths

- ./scripts/localMicrodata.py: script that can be run locally on to transform
  a file into RDF (on the standard output). Run the script with "-h" to
  get the available flags.

- ./Doc-pyMicrodata: (epydoc) documentation of the classes and functions

- ./generatePyMicrodataDoc: a shell script to generate the documentation (using epydoc)

- ./epydoc.css: the CSS file the documentation generation uses (it is then copied to the documentation area itself)

The package primarily depends on:
 - RDFLib<http://rdflib.net>. Version 3.2.0 or higher is strongly recommended.
 - html5lib<http://code.google.com/p/html5lib/> (in the additional packages folder)
 - pyRdflibExtras for a better (and more complete) serialization; is part of the pyrdfa3 package on github: https://github.com/RDFLib/pyrdfa3
    
The package has been tested on Python version 2.4 and higher. Python 2.6 is strongly recommended. The package
does not run with Python 3.

For the details on the conversion of Microdata to RDF, see:

http://www.w3.org/TR/2012/NOTE-microdata-rdf-20120308/


Release notes (starting from version 1.0)
=========================================

- this is the first fully released version

