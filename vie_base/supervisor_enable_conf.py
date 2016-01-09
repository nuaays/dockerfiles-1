#!/usr/bin/env python

import sys
import os

AVAIL_DIR = '/etc/supervisor/conf-available/%s.conf'
CONF_DIR = '/etc/supervisor/conf.d/%s.conf'

if len(sys.argv) <= 1:
    print "Incorrect number of parameters"
else:
    for filename in sys.argv[1:]:
        if os.path.isfile(AVAIL_DIR % filename):
            os.symlink(AVAIL_DIR % filename, CONF_DIR % filename)
        else:
            print "File", filename, "doesn't exist"
