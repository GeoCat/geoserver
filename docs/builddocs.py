import os
import shutil
import subprocess
import argparse


'''
This script generates documentation based on the content of the current
repo, for all the documentation branches (named "docs-[version_name]")

If the '--current' option is used, a version corresponding to the current
development version is generated instead, and created in a folder named 
"latest"

The script file should be located in the documentation folder (with sphinx 
files under ./source folder)

You can specify the output folder in which docs are to be produced, by using 
the '--output [path]' argument. If not used, the documentation will be created 
under the ./build folder. 
'''

NAME = "geoserver-enterprise"
DOC_BRANCH_PREFIX = "docs-"

toreplace = {"introduction/license.rst": [("/../../../../", "/../../geoserver/")],
            "services/wps/processes/gs.rst": [("../../../../../../../", "../../../../../geoserver/")]}

def sh(commands):
    if isinstance(commands, str):
        commands = commands.split(" ")
    out = subprocess.Popen(commands, stdout=subprocess.PIPE)
    stdout, stderr = out.communicate()
    return stdout.decode("utf-8")

def clean(folder):
    print("Cleaning build folder")
    shutil.rmtree(folder, ignore_errors=True)

def copycommunity():
    print("Copying geoserver user guide to staging")    
    gsdocssource = os.path.join(os.path.dirname(os.getcwd()), "geoserver", "doc", "en", "user", "source")
    gsdocsdest = os.path.join(os.getcwd(), "staging")
    for path in os.listdir(gsdocssource):
        src = os.path.join(gsdocssource, path)
        if os.path.isdir(src):            
            dst = os.path.join(gsdocsdest, path)
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    for path, changes in toreplace.items():
        filepath = os.path.join(gsdocsdest, path)
        with open(filepath) as f:
            txt = f.read()
        for old, new in changes:
            txt = txt.replace(old, new)
        with open(filepath, "w") as f:
            f.write(txt)

def copyenterprise():
    print("Copying enterprise docs to staging")    
    docssource = os.path.join(os.getcwd(), "src")
    docsdest = os.path.join(os.getcwd(), "staging")
    if os.path.exists(docsdest):
        shutil.rmtree(docsdest)   
    shutil.copytree(docssource, docsdest)

def builddocs(current, folder):
    refs = getrefs()
    if current:
        buildref(None, folder, "latest")
    else:
        for ref in refs:
            buildref(ref, folder)

def getrefs():
    refs = []
    branches = sh("git branch -r").splitlines()
    for line in branches:
        fullname = line.strip().split(" ")[0]
        name = fullname.split("/")[-1]
        if name.startswith(DOC_BRANCH_PREFIX):          
            refs.append(fullname)
    return refs

def buildref(ref, folder, versionname=None):
    versionname = versionname or ref.split("/")[-1].split(DOC_BRANCH_PREFIX)[-1]
    print("Building project '%s' at version '%s'..." % (NAME, versionname or ref)) 
    if ref is not None:
        sh("git checkout {}".format(ref))

    sourcedir = os.path.join(os.getcwd(), "staging")
    builddir = os.path.join(folder, versionname or ref)
    doctrees = os.path(join, builddir, ".doctrees"+versionname)
    if os.path.exists(builddir):
        shutil.rmtree(builddir)
    os.makedirs(builddir)
    sphinxbuild = "sphinx-build -a -j auto -d {} {} {}".format(doctrees, sourcedir, builddir)
    print(sphinxbuild);
    sh(sphinxbuild)

def main():
    parser = argparse.ArgumentParser(description='Build documentation.')
    parser.add_argument('--output', help='Output folder to save documentation')
    parser.add_argument('--clean', dest='clean', action='store_true', help='Clean output folder')
    parser.add_argument('--current', dest='current', action='store_true', help='Build current branch')
    parser.add_argument('--nocopy', dest='nocopy', action='store_true', help='Do not copy user guide docs to staging docs folder')

    args = parser.parse_args()

    folder = args.output or os.path.join(os.getcwd(), "build")

    if args.clean:
        clean(folder)

    if not args.nocopy:
        copyenterprise()
        copycommunity()

    builddocs(args.current, folder)

if __name__ == "__main__":
    main()
