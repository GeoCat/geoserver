import os
import shutil
import subprocess
import argparse


'''
This script generates documentation based on the content of the current
repo, for all the documentation branches (named "docs-[version_name]")

If the '--addmaster' option is used, a version corresponding to the current
development version is also generated, and created in a folder named "latest"

The script file should be located in the documentation folder (with sphinx 
files under ./source folder)

You can specify the output folder in which docs are to be produced, by using 
the '--output [path]' argument. If not used, the documentation will be created 
under the ./build folder. 
'''

NAME = "geoserver-enterprise"
DOC_BRANCH_PREFIX = "docs-"

def sh(commands):
    if isinstance(commands, str):
        commands = commands.split(" ")
    out = subprocess.Popen(commands, stdout=subprocess.PIPE)
    stdout, stderr = out.communicate()
    return stdout.decode("utf-8")

def clean(folder):
    print("Cleaning output folder")
    shutil.rmtree(folder, ignore_errors=True)

def copycommunity():
    print("Copying community docs")    
    gsdocssource = os.path.join(os.path.dirname(os.getcwd()), "geoserver", "doc", "en", "user", "source")
    gsdocsdest = os.path.join(os.getcwd(), "src", "community")
    if os.path.exists(gsdocsdest):
        shutil.rmtree(gsdocsdest)
    shutil.copytree(gsdocssource, gsdocsdest)
    conffile = os.path.join(gsdocsdest, "conf.py")
    os.remove(conffile)

def builddocs(addmaster, folder):
    refs = getrefs()
    if addmaster:
        buildref("master", folder, "latest")
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

    sourcedir = os.path.join(os.getcwd(), "src")
    builddir = os.path.join(folder, versionname or ref)
    if os.path.exists(builddir):
        shutil.rmtree(builddir)
    os.makedirs(builddir)
    sh("sphinx-build -a {} {}".format(sourcedir, builddir))

def main():
    parser = argparse.ArgumentParser(description='Build documentation.')
    parser.add_argument('--output', help='Output folder to save documentation')
    parser.add_argument('--clean', dest='clean', action='store_true', help='Clean output folder')
    parser.set_defaults(clean=False)
    parser.add_argument('--addmaster', dest='addmaster', action='store_true', help='Build also master branch')
    parser.add_argument('--nocopy', dest='nocopy', action='store_true', help='Do not copy community docs to source docs folder')
    parser.set_defaults(nocopy=False)

    args = parser.parse_args()

    folder = args.output or os.path.join(os.getcwd(), "build")

    if args.clean:
        clean(folder)

    if not args.nocopy:
        copycommunity()

    builddocs(args.addmaster, folder)
    sh("git checkout master")

if __name__ == "__main__":
    main()
