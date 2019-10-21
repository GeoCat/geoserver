# GeoCat Enterprise Theme

Module packaging up css and image resources for use by GeoServer administration web application.

GeoServer administration screens are defined using the Apache Wicket framework.

Contents

* src/java Defines a GeoServerEnterpriseTheme bean providing page header contributions 
* src/resources Provides static CSS and image resources

GeoServer HeaderContribution extension point is used to contribute specific files like `CSSFilename` and `faviconFilename`. GeoServerEnterpriseTheme uses this extension point to contribute static resources.

CSS `geoserver_enterprise.css` is used to overide the contents of `geoserver.css`. Any content, such as `img/logo.png`, that are not desired by this theme must be overriden.

```css
#header a {
  background: url(enterprise/geoserver_enterprise_logo.png) no-repeat;
}
```