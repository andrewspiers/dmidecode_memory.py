#!/usr/bin/env python
""" Report the capacity of each stick of installed memory. Must be run as root
or with sudo.
"""

# python-dmidecode is in debian and RedHat distros
import dmidecode
import os
import sys

if os.geteuid() != 0:

    sys.stderr.write(__doc__)
    # by continuing here, we get to keep the nice warnings that the dmidecode
    # library produces.

m = dmidecode.memory()

for x in m.iteritems():
    try:
        print(x[1]['data']['Size'])
    except KeyError:
        pass
