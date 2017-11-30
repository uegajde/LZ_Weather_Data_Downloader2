from datetime import datetime
from datetime import timedelta
import dfdnt.urlgenhelper

now = datetime.utcnow()


def geturl(timeConfigure, target):
    filenamelist = []
    fixtimeshift = timedelta(0)

    if target == "JMA_Weather_Chart_1":
        # example : http://www.jma.go.jp/jp/metcht/pdf/kosou/aupq35_00.pdf (only one)
        mode = 1
        extension = "pdf"
        base_url = "http://www.jma.go.jp/jp/metcht/pdf/kosou/"
        filenamelist.append("aupq35_00")
        filenamelist.append("aupq35_12")
        filenamelist.append("aupq78_00")
        filenamelist.append("aupq78_12")
    elif target == "JMA_Weather_Chart_2":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_2017112715.pdf   (every 6  hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_2017112621.pdf (every 12 hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_2017042509.pdf (every 12 hr)
        mode = 0
        datatz = +9
        timelabelformat = "%Y%m%d%H"
        extension = "pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filename = "ASAS_" + timelabel
            filenamelist.append(filename)
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hour", 0, 12, now)
        if timeConfigure.density[target] == 6:
            density = 12
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], density, timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filename = "AUPQ78_" + timelabel
            filenamelist.append(filename)
            filename = "AUPQ35_" + timelabel
            filenamelist.append(filename)
    elif target == "JMA_WaterVapor_Image":
        # example : http://www.jma.go.jp/jp/gms/imgs/0/watervapor/1/201711280020-00.png (every 10 min)
        mode = 0
        datatz = +9
        timelabelformat = "%Y%m%d%H%M-00"
        extension = "png"
        base_url = "http://www.jma.go.jp/jp/gms/imgs/0/watervapor/1/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Surface_Weather_Chart":
        # example : http://www.cwb.gov.tw/V7/forecast/fcst/Data/2014-0508-0600_SFCcombo.jpg (every 6 hr)
        mode = 0
        datatz = +0
        timelabelformat = "%Y-%m%d-%H00_SFCcombo"
        extension = "jpg"
        base_url = "http://www.cwb.gov.tw/V7/forecast/fcst/Data/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Skew":
        # example : http://www.cwb.gov.tw/V7/station/Data/SKW_46692.pdf (only one)
        mode = 1
        timelabelformat = "%Y-%m%d-%H00"
        extension = "pdf"
        base_url = "http://www.cwb.gov.tw/V7/station/Data/"
        filenamelist.append("SKW_46692")
        filenamelist.append("SKW_46699")
        filenamelist.append("SKW_46750")
    elif target == "CWB_Radar":
        # example : http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_201605161930.png (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "CV1_3600_%Y%m%d%H%M"
        extension = "png"
        base_url = "http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/"
        if timeConfigure.density[target] != 10:
            multiplier = timeConfigure.density[target]
        else:
            multiplier = 10
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("min", 0, multiplier, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Satellite_Visible":
        # example : http://www.cwb.gov.tw/V7/observe/satellite/Data/sbo/sbo-2016-08-12-19-50.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "sbo-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "http://www.cwb.gov.tw/V7/observe/satellite/Data/sbo/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Satellite_Infrared":
        # example : http://www.cwb.gov.tw/V7/observe/satellite/Data/s3q/s3q-2016-08-12-23-30.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "s3q-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "http://www.cwb.gov.tw/V7/observe/satellite/Data/s3q/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Surface_Temperature":
        # example : http://www.cwb.gov.tw/V7/observe/temperature/Data/2014-04-20_2000.GTP.jpg (every 1 hr)
        mode = 0
        datatz = +8
        timelabelformat = "%Y-%m-%d_%H00.GTP"
        extension = "jpg"
        base_url = "http://www.cwb.gov.tw/V7/observe/temperature/Data/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hr", 0, 1, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_Precipitation":
        # example : http://www.cwb.gov.tw/V7/observe/rainfall/Data/hka09100.jpg (every 30 min)
        mode = 0
        datatz = +8
        timelabelformat = "%m%d%H%M"
        extension = "jpg"
        base_url = "http://www.cwb.gov.tw/V7/observe/rainfall/Data/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("min", 0, 30, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            monlabel = int(timelabel[0:2])
            if monlabel == 10:
                monlabel = "a"
            elif monlabel == 11:
                monlabel = "b"
            elif monlabel == 12:
                monlabel = "c"
            monlabel = str(monlabel)
            filename = "hk" + monlabel + timelabel[2:7]
            filenamelist.append(filename)
    elif target == "CWB_850hpa_WindSpeed_Streamline":
        # example : http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/GFS_14041918_DS2-GE_000.gif (every 6 hr)
        mode = 0
        datatz = +0
        timelabelformat = "GFS_%y%m%d%H_DS2-GE_000"
        extension = "gif"
        base_url = "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif target == "CWB_850hpa_RH_Streamline":
        # example : http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/GFS_15020200_D51D2S-GE_000.gif (every 6 hr)
        mode = 0
        datatz = +0
        timelabelformat = "GFS_%y%m%d%H_D51D2S-GE_000"
        extension = "gif"
        base_url = "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/"
        fixtimeshift = dfdnt.urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = dfdnt.urlgenhelper.gettimelabel(
            timeConfigure.period[target], timeConfigure.density[target], timeConfigure.unit[target], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    return mode, base_url, filenamelist, extension
