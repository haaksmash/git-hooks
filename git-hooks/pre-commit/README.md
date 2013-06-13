# pre-commit

The `pre-commit` hook is used to inspect the snapshot that’s about to be
committed, to see if you’ve forgotten something, to make sure tests run, or to
examine whatever you need to inspect in the code. Exiting non-zero from this
hook aborts the commit, although you can bypass it with git commit --no-verify.
You can do things like check for code style (run lint or something equivalent),
check for trailing whitespace (the default hook does exactly that), or check
for appropriate documentation on new methods.

## copyrighter

Adds a copyright notice to the top of every ADDED file

## pypi_readme_synchronizer

Found this one useful for handling projects uploaded to PyPi; given a
github-style README, this hook will make a README.txt to reflect it in a way
that PyPi will display, since PyPi cries at files with the .rst extension.
