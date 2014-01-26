# post-merge

The `post-merge` hook runs after a successful merge command. You can use it to
restore data in the working tree that Git can’t track, such as permissions
data. This hook can likewise validate the presence of files external to Git
control that you may want copied in when the working tree changes.

## sass_compiler

Compiles sass files to css files, using `SASS_DIR` and `CSS_DIR` environment
variables to find sources and place the results, respectively. Both default to
the current directory.
