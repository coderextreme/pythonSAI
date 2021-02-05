#!/bin/sh

# Run the Test Suite

# accepts files with .x3d extension
export PROCESSORS=${PROCESSORS-8}

. ./profile.sh

javac -cp "saxon9he.jar:." RunSaxon.java

ls *.x3d | xargs -P $PROCESSORS java -cp "saxon9he.jar:." RunSaxon ---overwrite | xargs -P $PROCESSORS ${NODE} json2py.js
