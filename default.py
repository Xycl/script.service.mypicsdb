#!/usr/bin/python
# -*- coding: utf8 -*-


import xbmc, xbmcaddon

import time
from os.path import join
from pprint import pformat

# Script constants
__settings__ = xbmcaddon.Addon()
__addon_id__ = "script.service.mypicsdb"

__language__ = __settings__.getLocalizedString
__homepath__ = __settings__.getAddonInfo('path').decode('utf-8')


class UpdateService():

    def start(self):
        
        # sleep at the beginning.
        startup_sleep = abs(int(__settings__.getSetting( "STARTUP_SLEEP" )))
        if startup_sleep > 0:
            time.sleep(startup_sleep)

        while not xbmc.abortRequested:

            try:
                sleep_period = abs(int(__settings__.getSetting( "SLEEP_PERIOD" )) * 60)

                if sleep_period > 0:
                    xbmc.log("Starting MyPicsDB Library Update", xbmc.LOGNOTICE)
                    script = u"%s,--refresh"% join( __homepath__, u"..", u"plugin.image.mypicsdb", u"scanpath.py")
                    xbmc.executebuiltin('XBMC.RunScript(%s)'%script.encode('utf-8'))                    

                # sleep at least 5 minutes
                if sleep_period < 300:
                    sleep_period = 300

                time.sleep(sleep_period)    

            except Exception, e:
                xbmc.log(pformat(e))


UpdateService().start()