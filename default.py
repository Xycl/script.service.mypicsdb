#!/usr/bin/python
# -*- coding: utf8 -*-


import xbmc, xbmcaddon

import time
from os.path import join
from pprint import pformat

# Script constants
__settings__       = xbmcaddon.Addon()
__addon_id__    = "script.service.mypicsdb"

__language__ = __settings__.getLocalizedString
__homepath__ = __settings__.getAddonInfo('path').decode('utf-8')

#__version__     = "1"

sleep_period = int(__settings__.getSetting( "SLEEP_PERIOD" ))

class FritzCallmonitor():

    def start(self):

        while not xbmc.abortRequested:

            try:
                xbmc.log("Starting MyPicsDB Library Update", xbmc.LOGNOTICE)
                script = u"%s,--refresh"% join( __homepath__, u"..", u"plugin.image.mypicsdb", u"scanpath.py")
                xbmc.executebuiltin('XBMC.RunScript(%s)'%script.encode('utf-8'))
                time.sleep(sleep_period)    

            except Exception, e:
                xbmc.log(pformat(e))


if sleep_period < 10:
    sleep_period = 10
    
if __settings__.getSetting( "STARTUP_SLEEP" ):
    time.sleep(int(__settings__.getSetting( "STARTUP_SLEEP" )))

FritzCallmonitor().start()