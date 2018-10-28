#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "120m4n"
"""Creacion de un archivo shapefile tipo punto
"""

import gdal
import fiona
from fiona.crs import from_epsg
import os
from shapely.geometry import mapping, Point
import time

start = time.time()

xy=['-73.11422580154978,7.118116751350779,0']

output = os.path.realpath('./shapefiles/temp_point.shp')

#proyeccion 
f_crs=from_epsg(4326)

# columnas contenidas en el archivo shapefile
schema = {
    'geometry': 'Point',
    'properties': {
                'TIPOPINTA'       :   'int:3',
                'X'                 :   'int:10',
                'Y'                 :   'int:10'

    }                
}

start = time.time()

with fiona.open(output,'w', driver='ESRI Shapefile', crs=f_crs, schema=schema) as c:
	for p in xy:
		x = float(p.split(',')[0])
		y = float(p.split(',')[1])
		point=Point(x,y)
		c.write({
			'geometry': mapping(point),
			'properties': {
				'TIPOPINTA'   	:   1,
				'X'           :   x,
				'Y'           :   y
					}
})
print("proceso finalizado")

elapsed = (time.time() - start)
print(' TIEMPO TOTAL DE PROCESAMIENTO')
print ('		' + str(elapsed)+" segundos")