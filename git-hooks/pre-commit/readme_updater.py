import os
import subprocess


def do_update():
    root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).strip()

    rreadme_fname = os.path.join(root_dir, "README.rst")
    preadme_fname = os.path.join(root_dir, "README.txt")

    lines = []
    with open(rreadme_fname, 'r') as real_readme:
        lines = real_readme.readlines()

    with open(preadme_fname, 'w+b') as f:
        for line in lines:
            if line.startswith(".. code"):
                line = '::\n'
            f.write(line)



files = [
    x for x in subprocess.check_output("git diff --cached --name-status", shell=True).split('\n')\
        if x and x[0] != "D"
]

changed_files = False

for statusline in files:
    mode, fname = statusline.split('\t')
    if fname.startswith("README"):
        print "Updating pypi readme..."
        readme_updater.do_update()

if changed_files:
    print "Please check that the modifications are correct and"
    print "re-commit."
    sys.exit(1)

