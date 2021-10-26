# GeoCat Data Directories

Uses a combination of `mvn` and `ant` to download and process data, and maven to assemble bundles for download.

Used to manage data directories:

* default - minimal setup for enterprise customers with no sample data
* standard - includes natural earth sample data for enterprise custoemrs, GeoCat Live, and testing
* demo - includes natural earth and larger range of sample data for training and the geocat website

Hint: Use `ant -p` to show main targets.

## Default Data Directory

The default data directory is located in `src/default`, to edit the data directory use `webapp-standard`:

```
cd ../webapp-standard
mvn jetty:run -DGEOSERVER_DATA_DIR=../src/default
```

Ant is used to package `src/default` as a zip:

```
ant default-data-dir
```

Maven packages everything for distribution:

```
mvn package
```

## Standard Data Directory

Ant is used to package download and process data into `src/standard/data` folder:

```
ant standard-data-dir
```

To edit the data directory use `webapp-standard`:

```
cd ../webapp-standard
mvn jetty:run -DGEOSERVER_DATA_DIR=../src/standard
```

Maven packages everything for distribution:

```
mvn package -Pstandard
```

## Demo Data Directory

Please run the following script to download data and unzip into the correct location:

```
ant demo-data-dir
```

To edit the data directory use `webapp-training`:

```
cd ../webapp-standard
mvn jetty:run -DGEOSERVER_DATA_DIR=../src/demo
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

We cache downloads in our nexus repository using:

```
mvn deploy:deploy-file -DgroupId=com.naturalearthdata \
                       -DartifactId=NE1_HR_LC_SR_W_DR   \
                       -Dversion=3.2.0 \
                       -Dfile=download/NE1_HR_LC_SR_W_DR.zip \
                       -Dpackaging=zip \
                       -DrepositoryId=geocat \
                       -Durl=https://nexus.geocat.net/repository/geoserver-geocat
```

```
mvn deploy:deploy-file -DgroupId=com.naturalearthdata \
                       -DartifactId=GRAY_HR_SR_W \
                       -Dversion=3.2.0 \
                       -Dfile=download/GRAY_HR_SR_W.zip \
                       -Dpackaging=zip \
                       -DrepositoryId=geocat \
                       -DgeneratePom=true \
                       -DgeneratePom.description="Gray Earth with Shaded Relief, Hypsography, and Flat Water" \
                       -Durl=https://nexus.geocat.net/repository/geoserver-geocat
                       
mvn deploy:deploy-file -DgroupId=com.naturalearthdata \
                       -DartifactId=GRAY_HR_SR_W \
                       -Dversion=3.2.0 \
                       -Dfile=download/GRAY_HR_SR_W.zip \
                       -Dpackaging=zip \
                       -DrepositoryId=geocat \
                       -DgeneratePom=true \
                       -DgeneratePom.description="Gray Earth with Shaded Relief, Hypsography, and Flat Water" \
                       -Durl=https://nexus.geocat.net/repository/geoserver-geocat
```

### geopackage

Several ogr targets are used by `install_custom_geopackage` to create a new geopackage:

* -point
* -lines
* -polygons

### shapefile

These targets are designed to be used via antcall, using data property:

```xml
<property name="data" value="${standard}"/>
<antcall target="install_ne1"/>
```

Downloads are fetched, if required, into `downloads` folder:

* -cultural-download
* -cultural
* -physical-download
* -physical

These targets are designed to be used via antcall, using data and features parameters:

```xml
<antcall target="-physical">
  <param name="features" value="geographic_lines"/>
  <param name="data" value="standard"/>
</antcall>
```

### imagry 

Tasks like `ne1_download`, `ne1_process` and `ne1_install` download imagry, and prepare it for use using gdal, and copy the result into the ``data`` folder.

### dem

Tasks like `etopo1_download`, `etopo1_process`, `etopo1_install` download the etopo1 dataset, and prepare it for use using gdal, and copy the result into the ``data`` folder.

In this case jpeg compression of innter tiles is not appropriate as the information is intended as measurements rather than as a visual.

### demo data

For specific datasets like `bmng` and `eo` considerably more processing is needed.

These steps match up with the training `L101` exercises and are considered demo material.