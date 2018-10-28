#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "120m4n"
"""
Revisar el tipo de metadata contenida en el schema (dBase.dbf) de un archivo shapefile
"""

import gdal
import fiona
import json
import os


#fname = os.path.realpath('./shapefiles/APOYOS_PD.shp')
fname = os.path.realpath('./shapefiles/SHAPE_PUNTOS/SISMICA_2D_AGOSTO_2013_PTOS.shp')
with fiona.open(fname) as source:
    source_driver = source.driver
    source_crs = source.crs
    source_schema = source.schema
print(source_driver)
print(source_crs)
print(json.dumps(source_schema, indent=2))