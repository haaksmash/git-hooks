import os
import subprocess


def compile_sass():
    sass_dir = os.environ.get("SASS_DIR", ".")
    css_dir = os.environ.get("CSS_DIR", ".")

    """compiles sass files into css"""
    return subprocess.check_call(
        "sass compile --sass-dir {} --css-dir {}".format(
            sass_dir, css_dir,
        )

if __name__ == "__main__":
    print "compiling sass to css..."
    if compile_sass():
        print "\tsomething went wrong!
        return 1
