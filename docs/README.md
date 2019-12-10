# GeoServer Enterprise Documentation

## Sphinx

Documentation is written using the sphinx documentation system using restructured text. Extensive use of directives are used to capture intent (command, menu-selection,gui-label,kbd) rather than marking text in italic or bold.

## Pavement 

Pavement is a python build tool equivalent to make or ant:

```
paver builddocs
open build/html/index.html
```



Before use, install paver:
```
pip install paver
```

For more information please see [geocat-documentation](https://github.com/volaya/geocat-documentation).

## Themes

A number of sphinx themes are available:

* [geocat-themes](https://github.com/GeoCat/geocat-themes)

These themes are managed as git submodules for ease of maintenance.

Before use please install the `read-the-docs theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`__, to install:

```
pip install sphinx_rtd_theme
```


