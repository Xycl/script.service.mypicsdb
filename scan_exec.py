#!/usr/bin/python
# -*- coding: utf8 -*-

import xbmc, xbmcaddon

from os.path import join
from pprint import pformat

# Script constants
__settings__ = xbmcaddon.Addon()
__homepath__ = __settings__.getAddonInfo('path').decode('utf-8')

def scan_exec():
    xbmc.log("scan_exec.py : Starting MyPicsDB Library Update", xbmc.LOGNOTICE)
    script = u"%s,--refresh"% join( __homepath__, u"..", u"plugin.image.mypicsdb", u"scanpath.py")
    xbmc.executebuiltin('XBMC.RunScript(%s)'%script.encode('utf-8'))                    

if __name__=="__main__":
    try:
	    scan_exec()
    except Exception, e:
        xbmc.log(pformat(e))
