import os
from paver.easy import *
import paver.doctools

```
Generate GeoServer Enterprise documentation.
```

options(
    setup=dict(
    name='GeoServer Enterprise Documentation',
    version="2.16.1",
    description="Documentation for GeoServer Enterprise distribution by GeoCat.",
    author="Jody Garnett",
    author_email="jody.garnett@geocat.net",
    
    sphinx=Bunch(
       builddir="build/html",
       sourcedir="src"
    )
}

@task
@needs('paver.doctools.html')
def builddocs():
    '''Create html docs and install into build/html'''
    builddocs = path()
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')    
    for product in products:
        productFolder = os.path.join(tmpDir, product)        
        refs = getrefs(productFolder)
        for refname, ref in refs.items():
            build_product_doc(productFolder, refname, ref)