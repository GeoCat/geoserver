# GeoServer Enterprise Documentation

## Sphinx

Documentation is written using the sphinx documentation system using restructured text. Extensive use of directives are used to capture intent (command, menu-selection,gui-label,kbd) rather than marking text in italic or bold.

```
pip install sphinx
```

We also make use of two sphinx extensions, to help process markdown files:

```
pip install recommonmark
```

and to copy code from the `code blocks`:
```
pip install sphinx-copybutton
```

## Themes

A number of sphinx themes are available:

* [geocat-themes](https://github.com/GeoCat/geocat-themes)

These themes are managed as git submodules for ease of maintenance.

## Building the documentation

To build the documentation, run

```
python builddocs.py
```

That builds the docs as they are in the current branch.

The resulting docs are stored in the ``build`` folder.

This script combines the documentation of the geoserver user guide and the ``src`` folder into a `staging` folder which is built into a single manual.

To quickly rebuild without recopying:

```
python builddocs.py --rebuild
```

To force everything to rebuild:

```
python builddocs.py --clean
```

To check for additional commands use `python builddocs.py --help`.

### Creating a release version of the documentation

To create a new release version of the documentation, follow these steps:

- Create a new branch at the desired point (ensure that the submodules point to the correct commits in their corresponding repos).

- The name of the folder that indicates the version is taken from the ``VERSIONNAME`` constant in the builddocs.py script. In the ``master`` branch, it should be ``latest``. Modify it to reflect the version name of the newly created branch.

- The documentation in the ``master`` branch, when built, shows a ribbon that indicates that it is a pre-release version. To remove that in the release branch, edit the ``conf.py`` file in the docs root folder and modify the following line, setting the value to ``False``:

	html_context = {'theme_is_prerelease': True}

### Automatic build and deployment

There is a [Jenkins job](https://eos.geocat.net/jenkins/job/build-geoserver-enterprise-docs-pipeline) that watches for the `docs` folder changes and build and publish the branch that has the latest change.

