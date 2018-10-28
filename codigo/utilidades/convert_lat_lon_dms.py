# -*- coding: utf-8 -*-
__maintainer__ = "https://en.proft.me/2015/09/20/converting-latitude-and-longitude-decimal-values-p/"
import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd;

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = dms2dd(parts[4], parts[5], parts[6], parts[7])

    return (lat, lng)

def parse_dms2(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], str(int(parts[2])+int(parts[3])/1000), parts[4])
    lng = dms2dd(parts[5], parts[6], str(int(parts[7])+int(parts[8])/1000), parts[9])

    return (lat, lng)
#usage
# dd = parse_dms("36°57'9' N 110°4'21' W")
print(parse_dms2("6°37'49.394' N 73°9'55.376' W"))