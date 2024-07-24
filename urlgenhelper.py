from datetime import datetime
from datetime import timedelta


class timeConfigure:
    period = {}
    unit = {}
    timeInterval = {}
    again = {}
    namelist = []

    def __init__(self, name, unit, period, timeInterval, again):
       timeConfigure.namelist.append(name)
       timeConfigure.period[name] = period
       timeConfigure.unit[name] = unit
       timeConfigure.timeInterval[name] = timeInterval
       timeConfigure.again[name] = again


def gettimelabel(period, timeInterval, unit, fixtimeshift, tformat, datatimezone, now):
    timelabels = []
    before = 0
    while before < period:
        if (unit == "minute") or (unit == "min"):
            timeshift = timedelta(0, int(-1 * 60 * before))
        elif (unit == "hour") or (unit == "hr"):
            timeshift = timedelta(0, int(-1 * 3600 * before))
        elif unit == "day":
            timeshift = timedelta(int(-1 * before))
        targettime = now + timeshift + fixtimeshift + timedelta(0, int(3600 * datatimezone))
        timelabels.append(targettime.strftime(tformat))
        before += timeInterval
    return timelabels


def getfixtimeshift(unit, shift, multiplier, now):
    start = 0
    if (unit == "minute") or (unit == "min"):
        end = 60
        tformat = "%M"
    elif (unit == "hour") or (unit == "hr"):
        end = 24
        tformat = "%H"

    for before in range(start, end):
        if (unit == "minute") or (unit == "min"):
            fixtimeshift = timedelta(0, int(-1 * 60 * before))
            tformat = "%M"
        elif (unit == "hour") or (unit == "hr"):
            fixtimeshift = timedelta(0, int(-1 * 3600 * before))
            tformat = "%H"
        elif unit == "day":
            fixtimeshift = timedelta(int(-1 * before))
            tformat = "%d"
        fixedtime = now + fixtimeshift
        if (int(fixedtime.strftime(tformat)) + shift) % multiplier == 0:
            break
    return fixtimeshift


def urlcomposer(base_url, filenamelist, extension, addDownloadTimeLabel):
    # url info
    urls = []
    filenamesToSaveAs = []
    localnow = datetime.now()
    timelable = localnow.strftime('_%Y-%m-%d-%H-%M')

    if addDownloadTimeLabel is False:
        for filename in filenamelist:
            urls.append(base_url + filename + '.' + extension)
            filenamesToSaveAs.append(filename + '.' + extension)
    elif addDownloadTimeLabel is True:
        for filename in filenamelist:
            urls.append(base_url + filename + '.' + extension)
            filenamesToSaveAs.append(filename + timelable + '.' + extension)
    return urls, filenamesToSaveAs
