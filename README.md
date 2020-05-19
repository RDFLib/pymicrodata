# pyMicrodata

A [Microdata](https://www.w3.org/TR/microdata/) distiller/parser library

[![DOI](https://zenodo.org/badge/9385/RDFLib/pymicrodata.svg)](http://dx.doi.org/10.5281/zenodo.14541)

[Microdata](https://www.w3.org/TR/microdata/) is a specification that defines new HTML attributes to embed simple 
machine-readable data in HTML documents. This a module to extract Microdata RDF from an HTML5 page. It implements the 
algorithm defined and published by the W3C Semantic Web Interest Group task force, in March 2012. The module can be 
used to produce serialized versions of the extracted graph, or simply an [RDFLib](https://github.com/RDFLib/rdflib) 
`Graph` Object.

The distribution contains:

- **./pyMicrodata**: the Python library. You should copy the directory
  somewhere into your PYTHONPATH. Alternatively, you can also run the

    `~$ python setup.py install`

  script in the directory.

- **./scripts/CGI_microdata.py**: can be used as a CGI script to invoke the library.
  It has to be adapted to the local server setup, namely in setting the right paths

- **./scripts/localMicrodata.py**: script that can be run locally on to transform
  a file into RDF (on the standard output). Run the script with "-h" to
  get the available flags.

- **./Doc-pyMicrodata**: (epydoc) documentation of the classes and functions

- **./generatePyMicrodataDoc**: a shell script to generate the documentation (using epydoc)

- **./epydoc.css**: the CSS file the documentation generation uses (it is then copied to the documentation area itself)

The package primarily depends on:

 - [RDFLib](https://github.com/RDFLib/rdflib). Version 3.2.0 or higher is strongly recommended.
 - [html5lib](http://code.google.com/p/html5lib/) (in the additional packages folder)
 - several details or simply a more complete serialization depends on the pyrdfa3 package on github: https://github.com/RDFLib/pyrdfa3. Although the basic RDF conversion works without this, some serializations may not be available and the vocabulary expansion mechanism would not work either. 
    
The package has been tested on Python 3.5+, in line with RDFlib.

For the details on the conversion of Microdata to RDF, see:

<https://www.w3.org/TR/microdata-rdf/>


### Release notes (starting from version 1.0)

- this is the first fully released version

- Version 2.0: adapted to the new version of the microdata->RDF note. Differences, and its effect on the code, are:
    - The content of the registry is greatly reduced, see Appendix C
    - Remove the vocab expansion flag (although probably wise to keep it on the top, entry level, and just remove it
    from the real processing, to avoid backward compatibility issues for deployed code

- Version 3.0: adapting it to Python3.8 (and hopefully higher). It also relies on 5.0.0 of RDFlib (at the time of writing this is still dev version)




