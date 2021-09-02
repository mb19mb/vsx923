#!/usr/bin/python

import subprocess, imp
v = imp.load_source("habridge.vsx", "/home/pi/habridge/skripte/vsx.py")
vsx = v.VSX()
vsx.leiser()
