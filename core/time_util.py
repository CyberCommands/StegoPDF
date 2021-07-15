import os
import time
import datetime



class TimeUtil:
    def getModTime(self, file):
        unixTimeStamp = os.path.getmtime(file)
        return datetime.datetime.fromtimestamp(unixTimeStamp)

    def setModTime(self, file, date):
        modTime = time.mktime(date.timetuple())
        os.utime(file, (modTime, modTime))