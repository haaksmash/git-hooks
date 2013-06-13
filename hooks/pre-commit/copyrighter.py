LICENSE = """
This file is part of Flowhub, a command-line tool to enable various
Git-based workflows that interacts with GitHub.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

ME = "Copyright (C) 2012 Haak Saxberg"


def get_copyright_and_comment(txt):
    got_copyright = ""
    got_licence = False
    getting_comment = False
    comment = []
    linenum = 0
    for line in txt.splitlines():
        linenum += 1

        def strip(s):
            return s.strip("\"\"\"")

        if line.startswith("\"\"\""):
            break
        if line.startswith("Copyright (C)"):
            got_copyright = strip(line)
            continue
        if got_copyright and line.startswith("You should have received a copy of the GNU General Public License"):
            got_licence = True
            continue
        if got_copyright and got_licence and line.startswith("Boston"):
            getting_comment = True
            continue

        if getting_comment and line != "":
            comment.append(strip(line))

    return got_copyright, comment, linenum


def generate_header(people, comment):
    header = "\"\"\"\n"
    for p in people:
        header += "%s\n" % p
    header += LICENSE
    for c in comment:
        header += "%s\n" % c
    header += "\"\"\"\n\n"
    return header


def update_py_source(filename):
    #print filename
    fdata = file(filename, "r+").read()
    if fdata.count("This file is part of Flowhub, a command-line tool to enable various"):
        #print "\tskip"
        return False
    elif fdata.count("You should have received a copy of the GNU General Public License"):
        old_author, comments, linenum = get_copyright_and_comment(fdata)
        header = generate_header([old_author, ME], comments)
        #print "\tupdate"
    else:
        linenum = 0
        header = generate_header([ME], [])
        #print "\tadd"

    f = file(filename, "w")
    f.write(header)
    for l in fdata.splitlines()[linenum:]:
        f.write(l)
        f.write("\n")

    return True

files = [
    x for x in subprocess.check_output("git diff --cached --name-status", shell=True).split('\n')\
        if x and x[0] != "D"
]

changed_files = False

print "Checking for copyright notices..."
for statusline in files:
    mode, fname = statusline.split('\t')
    if mode == "A" and fname.endswith('.py'):
        if copyrighter.update_py_source(fname):
            subprocess.check_output("git add {}".format(fname), shell=True)
            print "\tAdded copyright notice to {}".format(fname)
            changed_files = True

if changed_files:
    print "Please check that the modifications are correct and"
    print "re-commit."
    sys.exit(1)
