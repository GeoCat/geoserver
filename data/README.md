# GeoCat Data Directories

Used to manage data directories:

* default - minimal setup with no sample data
* standard - includes natural earth sample data

Hint: Use `ant -p` to show main targets.

## Default Data Directory

Please run the following script to package up the default data directory as a zip:

```
ant default
```

If you wish to use the data directory directly:

```
export GEOSERVER_DATA_DIR=`cd default; pwd`
```

## Standard Data Directory

Please run the following script to download data and unzip into the correct location:

```
ant standard
```

If you wish to use the data directory directly:

```
export GEOSERVER_DATA_DIR=`cd standard; pwd`
```

## Downloading and installing data

The ant `build.xml` contains other targets that can be used to download and install content.

Hint: Use `ant -p -v` to show other targets.

Install targets copy data into a data folder:

* install_custom_geopackage
* install_custom_shapefiles
* install_dem
* install_gray
* install_ne1
* install_quickstart_geopackage
* install_quickstart_shapefiles
* install_quickstart_shapefiles_all

These targets are designed to be used via antcall, using data property:

```xml
<property name="data" value="${standard}"/>
<antcall target="install_ne1"/>
```

Downloads are fetched, if required, into `downloads` folder:

* _cultural
* _physical

These targets are designed to be used via antcall, using data and features parameters:

```xml
<antcall target="_physical">
  <param name="features" value="geographic_lines"/>
  <param name="data" value="standard"/>
</antcall>
```

Finally several ogr targets are used by `install_custom_geopackage` to create a new geopackage:

* _ogr_point
* _ogr_lines
* _ogr_polygons