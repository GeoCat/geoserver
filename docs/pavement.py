import os
from paver.easy import *
import paver.doctools

'''
Generate GeoServer Enterprise documentation.
'''
options(
    setup=dict(
        name='GeoServer Enterprise Documentation',
        version='2.16.1',
        description='Documentation for GeoServer Enterprise distribution by GeoCat.',
        author='Jody Garnett',
        author_email='jody.garnett@geocat.net',
   ),
    sphinx=Bunch(
       sourcedir='src',
       docroot='.',
       builder='html',
       doctrees='build/doctrees',
       builddir='build',
       apidir = None
    )
)

@task
@needs('paver.doctools.html')
def builddocs():
    '''
    Create html docs and install into build/html
    '''