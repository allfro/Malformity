#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash, MaliciousProcess
from common.malwr import build

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
]

#@superuser
@configure(
    label='TODO: To Something [Hello World]',
    description='TODO: Returns a Something entity with the phrase "Hello Word!"',
    uuids=[ 'TODO something.v2.SomethingToPhrase_HelloWorld' ],
    inputs=[ ( 'TODO: Some Set', SomethingEntity ) ],
    debug=True
)
def dotransform(request, response):
    #Build Request
    page = build(request.value)
    
    #Find the Process tree and extract processes
    procs = page.find("ul", {"id" : "tree"}).findNext('li')
    elements = procs.findAll("span", {"class" : "mono"})
    for element in elements:
    	text = element.find(text=True)
    	response += MaliciousProcess(text)
    
    return response