#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "120m4n"
"""Creacion de un archivo geojson tipo linea
"""

from shapely.geometry import mapping, LineString
import fiona
import os


#line = LineString([(-98.98234, 19.38234) ,(-98.990341,19.342345),(-98.992449, 19.378621),(-98.991299, 19.378233),(-98.992349999, 19.377381)])

x = [-73.1142258,-73.11394629,-73.11353373,-73.11320092,-73.11284128,-73.11281468,-73.11252844,-73.11239524,-73.1122848,-73.11214811,
-73.11199157,-73.1120583,-73.11256352,-73.11323472,-73.11373994,-73.1140922,-73.1141244,-73.11410955,-73.11412161,-73.11419983]

y = [7.118116751,7.118175041,7.118246005,7.118330478,7.11847423,7.118474126,7.118552182,7.118604446,7.11795079,7.117211254,7.116445243,
7.11638612,7.116421091,7.116522693,7.11655766,7.116598627,7.116862684,7.117251925,7.11756209,7.117958292]

xy = list(zip(x,y))

line = LineString(xy)

outputfile = os.path.realpath('./shapefiles/linea.geojson')

schema = {'geometry': 'LineString',
        'properties': {
        'id': 'int', 
        'name': 'str'
        }
}

with fiona.open(outputfile,'w','GeoJSON', schema) as gj:
    gj.write({
            'geometry':mapping(line), 
            'properties':{
                'id'    :   0, 
                'name'  :   'test'
                }
    })
print("ok")