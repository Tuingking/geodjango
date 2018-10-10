# Initial Setup

## Docker

Install PostGIS:
```sh
docker run -p 5432:5432 --name postgis -e POSTGRES_PASSWORD=password \
  -e POSTGRES_USER=root -e POSTGRES_DB=geodjango -d mdillon/postgis
```

Enter to docker console:
```sh
docker exec -it postgis bash -l 
```

## Postgres

Enter to postgres console:
```sh
psql -h localhost -p 5432 -U root -d geodjango
```

Postgres Command:
```sh
\l              : show databases
\c <database>   : use database
\d              : show tables
```

## Generate model and Insert to table

Generate django model from `.shp` file

```sh
python manage.py ogrinspect indonesia/data/gadm36_IDN_1.shp ProvinsiBorder --srid=4326 --mapping --multi

python manage.py ogrinspect indonesia/data/gadm36_IDN_2.shp KabupatenBorder --srid=4326 --mapping --multi

python manage.py ogrinspect indonesia/data/gadm36_IDN_3.shp KecamatanBorder --srid=4326 --mapping --multi

python manage.py ogrinspect indonesia/data/gadm36_IDN_4.shp KelurahanBorder --srid=4326 --mapping --multi
```

Insert `.shp` file into table through python shell

```python
from indonesia import load

load.run()
```

