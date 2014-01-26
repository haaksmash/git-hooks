import os
import subprocess


def compile_sass():
    """compiles sass files into css"""

    sass_dir = os.environ.get("SASS_DIR", ".")
    css_dir = os.environ.get("CSS_DIR", ".")
    return subprocess.check_call(
        ["sass" "--update", "{}:{}".format(sass_dir, css_dir)],
    )

if __name__ == "__main__":
    print "compiling sass to css..."
    if compile_sass():
        print "\tsomething went wrong!
        1
