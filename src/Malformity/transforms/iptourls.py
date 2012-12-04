#!/usr/bin/env python

from sploitego.config import config
from sploitego.framework import configure
from sploitego.maltego.message import URL, IPv4Address, Label
from sploitego.maltego.utils import debug
from sploitego.iptools.ip import IPAddress
from cif import Client


__author__ = 'Kyle Maxwell'
__copyright__ = 'Copyright 2012, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Kyle Maxwell'
__email__ = '@kylemaxwell'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label="To URLs [CIF]",
    description="This transform returns URLs with data from CIF queries based on IP address.",
    uuids=['cif.v2.IPv4AddressToURLs_CIF'],
    inputs=[('Collective Intelligence', IPv4Address)]
)
def dotransform(request, response):

    ipaddr = IPAddress(request.value)

    debug('Entity value received %s' % ipaddr)

    cifr = Client(config['cif/host'], config['cif/apikey']).GET(str(ipaddr), simple=True)
    debug('D:CIF output: %s\n' % cifr)

    # only returning some core values for now
    # TODO: should we add ASN, etc?
    for result in cifr:
    # we only care about results that actually return a URL, other results are not helpful here
        if result['alternativeid']:
            e = URL(result['alternativeid'])
            e += Label("Description", result['description'])
            e += Label("Confidence", result['confidence'])
            e += Label("General Impact", result['impact'])
            e += Label("Time of Observation", result['detecttime'])
            response += e

    return response
