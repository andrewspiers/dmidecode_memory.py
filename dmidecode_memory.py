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

count = 0
for x in m.iteritems():
    size = None
    try:
        size = x[1]['data']['Size']
        count += 1
    except KeyError:
        pass
    if size is None:
        pass
    else:
        print (size)
print('{} sticks in total.'.format(count))
