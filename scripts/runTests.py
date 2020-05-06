#!/usr/bin/env python
"""
Run the microdata testing locally
"""
# You may want to adapt this to your environment...
import sys
sys.path.append("..")
import glob
from pyMicrodata import pyMicrodata
from rdflib import Graph

###########################################

# marshall all test HTML files
test_path      = "../tests/"
test_html_files = glob.glob(test_path + "*.html")

# create the testing object
processor = pyMicrodata()

# for each HTML file...
for f in test_html_files:
	print("trying {}".format(f))
	g1 = Graph().parse(data=processor.rdf_from_source(f), format="turtle")
	g2 = Graph().parse(f.replace("html", "ttl"), format="turtle")
	assert g1.isomorphic(g2)
