Installation
---
```sh
brew install gdal
```

Convert .shp file to JSON
---
```sh
$ ogr2ogr -f GeoJSON -t_srs crs:84 OUTPUT.json SHP_FILE_GOES_HERE.shp
```

Examine shapefile metadata
---
```sh
$ ogrinfo SHP_FILE_GOES_HERE.shp

-- or --

$ ogrinfo -so TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3
```

