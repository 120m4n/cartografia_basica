#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "120m4n"
"""Creacion de un archivo geojson de puntos
"""




from shapely.geometry import mapping, Point
import fiona
import os


x = [-73.1142258,-73.11394629,-73.11353373,-73.11320092,-73.11284128,-73.11281468,-73.11252844,-73.11239524,-73.1122848,-73.11214811,
-73.11199157,-73.1120583,-73.11256352,-73.11323472,-73.11373994,-73.1140922,-73.1141244,-73.11410955,-73.11412161,-73.11419983]

y = [7.118116751,7.118175041,7.118246005,7.118330478,7.11847423,7.118474126,7.118552182,7.118604446,7.11795079,7.117211254,7.116445243,
7.11638612,7.116421091,7.116522693,7.11655766,7.116598627,7.116862684,7.117251925,7.11756209,7.117958292]


outputfile = os.path.realpath('./shapefiles/punto.geojson')

schema = {'geometry': 'Point',
        'properties': {
        'id': 'int', 
        'name': 'str'
        }
}

with fiona.open(outputfile,'w','GeoJSON', schema) as gj:
    for p in zip(x,y):
        point = Point(p)
        gj.write({
            'geometry':mapping(point), 
            'properties':{
                'id'    :   0, 
                'name'  :   'test'
                }
    })
print("ok")