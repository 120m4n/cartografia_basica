# cartografia_basica
Creación de archivos geograficos (shapefile,geojson) tipo punto y tipo linea a partir de archivos csv con coordenadas

## Requisitos

- Crear ambiente virtual
conda create --name carto python=3.6

- activar ambiente
activate carto

### Instalar los paquetes necesarios: 64 bits
./paquetes/64bits
```
  pip install GDAL-2.3.2-cp36-cp36m-win_amd64.whl
  pip install Fiona-1.7.13-cp36-cp36m-win_amd64.whl
  pip install Shapely-1.6.4.post1-cp36-cp36m-win_amd64.whl
```
### Instalar los paquetes necesarios: 64 bits
./paquetes/32bits
```
  pip install GDAL-2.2.4-cp36-cp36m-win32.whl
  pip install Fiona-1.7.11.post1-cp36-cp36m-win32.whl
  pip install Shapely-1.6.4.post1-cp36-cp36m-win32.whl
```
### Ejm: Creacion de punto
```python
import gdal
import fiona
from fiona.crs import from_epsg
import os
from shapely.geometry import mapping, Point

xy=['-73.11422580154978,7.118116751350779,0']

output = os.path.realpath('./shapefiles/temp_point.shp')

#proyeccion 
f_crs=from_epsg(4326)

# columnas contenidas en el archivo shapefile
schema = {
    'geometry': 'Point',
    'properties': {
                'TIPOPINTA':   'int:3',
                'X'  :   'int:10',
                'Y'  :   'int:10'

    }                
}

with fiona.open(output,'w', driver='ESRI Shapefile', crs=f_crs, schema=schema) as c:
	for p in xy:
		x = float(p.split(',')[0])
		y = float(p.split(',')[1])
		point=Point(x,y)
		c.write({
			'geometry': mapping(point),
			'properties': {
				'TIPOPINTA':   1,
				'X':   x,
				'Y':   y
					}
})
print("proceso finalizado")
```
### Explicacion
```
import gdal
import fiona
from fiona.crs import from_epsg
import os
from shapely.geometry import mapping, Point
```
1.  importamos las liberias necesarias
  *  Gdal es la base geografia
  *  fiona contiene los drives y herramientas que crean los objetos geograficos
  *  shapely me permite crear los elementos geograficos (punto, linea, poligono)

2. Alistamos las coordenadas del punto
```
xy=['-73.11422580154978,7.118116751350779,0']
coordenadas geográficas o coordenadas cartesianas o planas
```
3. Seleccionamos el [marco espacial](https://mappinggis.com/2016/04/los-codigos-epsg-srid-vinculacion-postgis/) 
```
#proyeccion 
f_crs=from_epsg(4326)
```


