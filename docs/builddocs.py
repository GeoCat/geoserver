import os
import shutil
import subprocess
import argparse


'''
This script generates documentation based on the content of the current
repo.

The script file should be located in the documentation folder (with sphinx 
files under ./source folder)

You can specify the output folder in which docs are to be produced, by using 
the '--output [path]' argument. If not used, the documentation will be created 
under the ./build folder. 
'''

VERSIONNAME = "latest"

toreplace = {"introduction/license.rst": [("/../../../../", "/../../../geoserver/")],
            "services/wps/processes/gs.rst": [("../../../../../../../", "../../../../../../geoserver/")]}

def sh(commands):
    if isinstance(commands, str):
        commands = commands.split(" ")
    out = subprocess.Popen(commands, stdout=subprocess.PIPE)
    stdout, stderr = out.communicate()
    return stdout.decode("utf-8")

def clean(folder):
    print("Cleaning build folder")
    shutil.rmtree(folder, ignore_errors=True)

def copycommunity(versionname):
    print("Copying geoserver user guide to staging")    
    gsdocssource = os.path.join(os.path.dirname(os.getcwd()), "geoserver", "doc", "en", "user", "source")
    gsdocsdest = os.path.join(os.getcwd(), "staging", versionname)
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

def copyenterprise(versionname):
    print("Copying enterprise docs to staging")    
    docssource = os.path.join(os.getcwd(), "src")
    docsdest = os.path.join(os.getcwd(), "staging", versionname)  
    shutil.copytree(docssource, docsdest)

def copytostaging(versionname):
    docsdest = os.path.join(os.getcwd(), "staging", versionname)
    if os.path.exists(docsdest):
        shutil.rmtree(docsdest)
    copyenterprise(versionname)
    copycommunity(versionname)

def builddocs(folder):
    currentHead = sh("git rev-parse --abbrev-ref HEAD").splitlines()[0]
    versionname = "latest" if currentHead == "master" else currentHead

    copytostaging(versionname)    
    sourcedir = os.path.join(os.getcwd(), "staging", versionname)
    builddir = os.path.join(folder, versionname)
    # doctrees = os.path.join(builddir, ".doctrees"+versionname)
    if os.path.exists(builddir):
        shutil.rmtree(builddir)
    os.makedirs(builddir)
    sphinxbuild = "sphinx-build -a -j auto {} {}".format(sourcedir, builddir)
    sh(sphinxbuild)

def main():
    parser = argparse.ArgumentParser(description='Build documentation.')
    parser.add_argument('--output', help='Output folder to save documentation')
    parser.add_argument('--clean', dest='clean', action='store_true', help='Clean output folder')

    args = parser.parse_args()

    folder = args.output or os.path.join(os.getcwd(), "build")

    if args.clean:
        clean(folder)

    builddocs(folder)


if __name__ == "__main__":
    main()
