# GeoServer Enterprise Documentation

## Sphinx

Documentation is written using the sphinx documentation system using restructured text. Extensive use of directives are used to capture intent (command, menu-selection,gui-label,kbd) rather than marking text in italic or bold.

```
pip install sphinx
```

## Themes

A number of sphinx themes are available:

* [geocat-themes](https://github.com/GeoCat/geocat-themes)

These themes are managed as git submodules for ease of maintenance.

Before use please install the `read-the-docs theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`__, to install:

```
pip install sphinx_rtd_theme
```

## builddocs.py

The python script ``builddocs.py`` is used to build documentation:

```
python builddocs.py
open build/latest/index.html
```

This script combines the documentation of the geoserver user guide and the ``src`` folder into a single manual.

